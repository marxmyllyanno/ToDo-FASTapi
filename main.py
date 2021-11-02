from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from datetime import date

app = FastAPI()

class Todo(BaseModel):
    assignment: str
    done: bool
    deadline: Optional[date]

lista = []

@app.post('/insert')
def insert(todo: Todo):
    try:
        lista.append(todo)
        return {'status': 'sucess'}
    except:
        return {'status': 'error'}

@app.post('/listing')
def listing(option: int = 0):
    if option == 0: #if the don't tell the option, or, if he informs option 0, it will return all the saved assignments
        return lista
    elif option == 1:
        return list(filter(lambda x: x.done == False, lista)) #if the user says option 1, it will only return the assignments that are not done
    elif option == 2:
        return list(filter(lambda x: x.done == True, lista)) #if the user says option 2, it will return the assignments that are already done

@app.get('/uniclist/{id}') #show the assignment you choose by the ID
def listing(id: int):
    try:
        return lista[id]
    except:
        return {'status': 'error'}

@app.post('/changestatus') #change the status of the assignmente
def changestatus(id: int):
    try:
        lista[id].done = not lista[id].done
        return {'status': 'sucess'}
    except:
        return {'status': 'error'}

@app.post('/delet') #delet the assignmente
def delete(id: int):
    try:
        del lista[id]
        return {'status': 'sucesso'}
    except:
        return {'status': 'error'}