from fastapi import APIRouter
user = APIRouter()

@user.get('/users')
def get_users():
    return {"Hola mundo"}

@user.post('/')
def post_raiz():
     return {"Hola aquí no hay nada, dirigete a /docs"}