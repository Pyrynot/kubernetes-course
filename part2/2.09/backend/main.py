from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from typing import List
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
import os
from contextlib import asynccontextmanager
import httpx

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


class TodoDB(Base):
    __tablename__ = 'todos'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    content = Column(String(140), nullable=False)

Base.metadata.create_all(bind=engine)

app = FastAPI()

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
    content: str

@app.get("/todos", response_model=List[TodoItem])
async def get_todos(db: Session = Depends(get_db)):
    todos = db.query(TodoDB).all()
    return todos

@app.post("/todos", response_model=TodoItem)
async def create_todo(todo: TodoItem, db: Session = Depends(get_db)):
    db_todo = TodoDB(content=todo.content)
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo

@app.post("/todos/random", response_model=TodoItem)
async def create_random_todo(db: Session = Depends(get_db)):
    url = get_random_wikipedia_article()
    todo_content = f"Read {url}"
    db_todo = TodoDB(content=todo_content)
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo
