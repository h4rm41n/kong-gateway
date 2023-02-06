from fastapi import FastAPI
import requests

app = FastAPI()

USERS_URL = "https://reqres.in/api/users"

@app.get('/')
async def users(page: int = 1):
    if page is not None:
        page = page
    else:
        page = 1

    try:
        user = requests.get(f'{USERS_URL}?page={page}')
        return {'messages': 'Load data users', 'data': user.json(), 'status': 200}
    except:
        return {'message': 'Ada kesalahan di server', 'status': 500}


@app.get('/{id}')
async def users(id: int):
    try:
        user_url = f'{USERS_URL}/{id}'
        user = requests.get(user_url)
        return {'message': 'Load data user', 'data': user.json(), 'status': 200}
    except:
        return {'message': 'Ada kesalahan di server', 'status': 500}