from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()


class Student(BaseModel):
    name : str
    rollno : str


my_students : list[Student] = [
    {"name": "khakachang","rollno": "d25cs202"},
    {"name": "Payel Debbarma","rollno": "d25cs211"}
]


@app.get("/")
async def root():
    return {"msg": "Hello World Updated"}


@app.get("/students", response_model=list[Student])
async def get_students() -> list[Student]:
    return my_students 