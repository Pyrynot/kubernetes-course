from fastapi import FastAPI
from sqlalchemy import create_engine, Column, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from contextlib import asynccontextmanager
import asyncio

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

app = FastAPI()

class Counter(Base):
    __tablename__ = 'counter'
    id = Column(Integer, primary_key=True, index=True)
    count = Column(Integer, default=0)

Base.metadata.create_all(bind=engine)

@asynccontextmanager
async def lifespan(app: FastAPI):
    db = SessionLocal()
    counter = db.query(Counter).get(1)
    if not counter:
        counter = Counter(id=1, count=0)
        db.add(counter)
        db.commit()
    db.close()
    yield

app = FastAPI(lifespan=lifespan)


@app.get("/")
def read_root():
    return {"message": "Service is up and running"}

@app.get("/pingpong")
def read_pingpong():
    with SessionLocal() as db:
        counter = db.query(Counter).get(1)
        if counter is None:
            counter = Counter(id=1, count=0)
            db.add(counter)
        counter.count += 1
        db.commit()
        response = f"pong {counter.count}"
    return response

@app.get("/pong_count")
def get_pong_count():
    with SessionLocal() as db:
        counter = db.query(Counter).get(1)
        count = counter.count if counter else 0
    return {"count": count}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8020)