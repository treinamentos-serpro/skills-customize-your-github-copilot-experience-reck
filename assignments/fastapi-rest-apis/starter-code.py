from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Simple Items API")


class Item(BaseModel):
    id: int
    name: str
    price: float = 0.0
    in_stock: bool = True


items = [
    {"id": 1, "name": "Laptop", "price": 999.99, "in_stock": True},
    {"id": 2, "name": "Mouse", "price": 29.99, "in_stock": False},
]


@app.get("/")
def read_root():
    return {"message": "Welcome to the Items API"}


@app.get("/items")
def get_items():
    return items


# TODO: Add POST, PUT/PATCH, and DELETE endpoints here
