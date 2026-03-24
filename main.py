from fastapi import FastAPI
from typing import List
import requests

app = FastAPI()

tasks = []


@app.post("/tasks/")
def create_task(title: str):
    task = {"id": len(tasks) + 1, "title": title}
    tasks.append(task)
    return task


@app.get("/tasks")
def list_tasks():
    return tasks


@app.put("/tasks/{task_id}")
def complete_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = True
            return task
    return {"error": "Task not found"}


@app.get("/external-users")
def get_external_users():
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    users = response.json()

    result = []
    for user in users:
        result.append({"name": user["name"], "email": user["email"]})

    return result
