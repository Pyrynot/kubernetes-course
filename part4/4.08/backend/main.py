from fastapi import FastAPI, Depends, HTTPException, Request
from pydantic import BaseModel, field_validator
from typing import List
from sqlalchemy import create_engine, Column, Integer, String, text, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
import os
from contextlib import asynccontextmanager
import httpx
import logging
import nats
import json

DATABASE_URL = os.getenv("DATABASE_URL")
NATS_URL = os.getenv("NATS_URL")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


async def init_nats():
    return await nats.connect(NATS_URL)

async def publish_event(event_type: str, data: dict):
    nc = await init_nats()
    message = {
        "event": event_type,
        "data": data
    }
    await nc.publish("todos.events", json.dumps(message).encode('utf-8'))
    await nc.drain()

class TodoDB(Base):
    __tablename__ = 'todos2'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    content = Column(String(140), nullable=False)
    done = Column(Boolean, default=False)

Base.metadata.create_all(bind=engine)

app = FastAPI()

logger = logging.getLogger(__name__)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_random_wikipedia_article():
    response = httpx.get("https://en.wikipedia.org/wiki/Special:Random")
    return response.headers['Location']



class TodoItem(BaseModel):
    id: int = None
    content: str
    done: bool = False

    class Config:
        orm_mode = True 

    @field_validator('content')
    def content_length(cls, v):
        if len(v) > 140:
            logger.warning(f"Attempted to create a to-do with content too long: {v}")
            raise ValueError('Todo content too long')
        return v

class TodoUpdate(BaseModel):
    done: bool

@app.get("/")
async def root():
    return {"ok": "deploy ok"}


@app.get("/todos", response_model=List[TodoItem])
async def get_todos(db: Session = Depends(get_db)):
    todos = db.query(TodoDB).all()
    return [TodoItem(id=todo.id, content=todo.content, done=todo.done) for todo in todos]



@app.post("/todos", response_model=TodoItem)
async def create_todo(todo: TodoItem, db: Session = Depends(get_db)):
    db_todo = TodoDB(content=todo.content, done=todo.done)
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    logger.info(f"Created to-do: {todo.content}")
    await publish_event("todo_created", {"id": db_todo.id, "content": db_todo.content, "done": db_todo.done})
    return TodoItem(id=db_todo.id, content=db_todo.content, done=db_todo.done)



@app.post("/todos/random", response_model=TodoItem)
async def create_random_todo(db: Session = Depends(get_db)):
    url = get_random_wikipedia_article()
    todo_content = f"Read {url}"
    db_todo = TodoDB(content=todo_content)
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    logger.info(f"Created random to-do: {todo_content}")
    return db_todo

@app.put("/todos/{todo_id}", response_model=TodoItem)
async def update_todo(todo_id: int, todo: TodoUpdate, db: Session = Depends(get_db)):
    db_todo = db.query(TodoDB).filter(TodoDB.id == todo_id).first()
    if db_todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    
    db_todo.done = todo.done
    db.commit()
    db.refresh(db_todo)
    
    logger.info(f"Updated to-do with ID {todo_id}: (Done: {todo.done})")
    await publish_event("todo_updated", {"id": db_todo.id, "content": db_todo.content, "done": db_todo.done})
    return TodoItem(id=db_todo.id, content=db_todo.content, done=db_todo.done)


@app.get("/healthz")
async def healthz():
    return {"status": "ok"}


@app.get("/readyz")
async def readyz(db: Session = Depends(get_db)):
    try:
        with SessionLocal() as db:
            db.execute(text('SELECT 1'))
        return {"status": "ready"}
    except Exception as e:
        logger.error(f"Readiness check failed: {e}")
        raise HTTPException(status_code=500, detail={"status": "unhealthy", "error": str(e)})


@app.exception_handler(ValueError)
async def value_error_handler(request: Request, exc: ValueError):
    logging.warning(f"Invalid to-do: {exc}")
    raise HTTPException(status_code=400, detail=str(exc))