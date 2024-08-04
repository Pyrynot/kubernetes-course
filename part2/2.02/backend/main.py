from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

todos = []

class TodoItem(BaseModel):
    content: str

@app.get("/todos", response_model=List[TodoItem])
async def get_todos():
    return todos

@app.post("/todos", response_model=TodoItem)
async def create_todo(todo: TodoItem):
    todos.append(todo)
    return todo