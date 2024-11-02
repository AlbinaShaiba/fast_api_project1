from typing import Annotated

from fastapi import FastAPI, Query, Path, Form, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import session

from core.schemas.item import Item
from core.database import connection
from core.models import User

class FormData(BaseModel):
    username: str
    password: str

app = FastAPI()

users = {
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four'
}

@app.post('/users')
@connection
async def add_user(username: str, password: str):
    new_user = User(username=username, password=password)
    session.add(new_user)
    await session.commit()


@app.post('/login')
async def login(data: Annotated[FormData, Form()]):
    data_dict = data.dict()
    return data_dict['username']

@app.get('/users/me', status_code=200)
async def get_current_user():
    return {'user_id': 'current_user'}
@app.get('/users/{user_id}', status_code=200)
async def read_user(user_id: Annotated[int, Path(title='The ID of the user')]):
    if not user_id in users:
        raise HTTPException(status_code=404)
    return users[user_id]

@app.get('/items', status_code=200)
async def read_item(
        q: Annotated[str | None, Query(min_length=3, max_length=10)] = None
):
    results = {'items': [{'item_id': 'Foo'}, {'item_id': 'Bar'}]}
    if q:
        results.update({'q': q})
    return results

@app.post('/items', status_code=201)
async def create_item(item: Item):
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({'price_with_tax': price_with_tax})
    return item_dict

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    return {'item_id': item_id, **item.dict()}