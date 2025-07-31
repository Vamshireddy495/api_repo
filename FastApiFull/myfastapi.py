from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import  Optional

app = FastAPI()

class Todo(BaseModel):
    todo_name:str = Field(...,description = 'Name of the task')
    todo_description:str = Field(...,description = 'Description of the task')
    todo_id:int = Field(...,description = "unique id")

class Update(BaseModel):
    todo_name:Optional[str] = Field(None,description = 'Name of the task')
    todo_description:Optional[str] = Field(None,description = 'Description of the task')
    # todo_id:Optional[int] = Field(...,description = "unique id")


all_todos = [Todo(todo_id = 1, todo_name='work',todo_description='try focusing'),
             Todo(todo_id = 2, todo_name='Study',todo_description='try focusing'),
             Todo(todo_id = 3, todo_name='Eat',todo_description='try focusing')]
# GET, post, delete, put
@app.get("/alltodos", response_model=list[Todo])
def get_all_todos():
    return all_todos


@app.get('/alltodos/{todo_id}', response_model = Todo)

def getAll_list(todo_id:int):
    for todo in all_todos:
        if todo.todo_id == todo_id:
            return todo
        
    
@app.put("/updatetodo/{todo_id}", response_model=Todo)

def update_todo(todo_id: int, update_data: Update):
    for todo in all_todos:
        if todo.todo_id == todo_id:
            if update_data.todo_name is not None:
                todo.todo_name = update_data.todo_name
            if update_data.todo_description is not None:
                todo.todo_description = update_data.todo_description
            return todo
    raise HTTPException(status_code=404, detail="Todo not found")


@app.post("/addtodo", response_model = Todo)

def addtodo(todo: Todo):
    for existing in all_todos:
        if existing.todo_id == todo.todo_id:
            raise HTTPException(status_code=400, detail="Todo with this ID already exists")
    all_todos.append(todo)
    return todo

@app.delete('/delete_todo/{todo_id}', response_model= Todo)
def deletetodo(todo_id : int):
    for index, todo in enumerate(all_todos):
        if todo.todo_id == todo_id:
            deletetodo = all_todos.pop(index)
            return deletetodo
    raise HTTPException(status_code=404, detail="Not available")
    




# class Todo(BaseModel):
#     todo_name : str = Field(...,min_length = 3, max_length = 512, description = 'Name of new todo')
#     todo_description : str = Field(..., description = 'give description')
#     todo_id :int 

# class Update(BaseModel):
#     todo_name : Optional[str] = Field(None,min_length = 3, max_length = 512, description = 'Name of new todo')
#     todo_description : Optional[str] = Field(None, description = 'give description')


# # all_todos = [{'todo_id' : 1, 'todo_name' : 'gym', 'todo_description' : 'try workout'},
# #             {'todo_id' : 2, 'todo_name' : 'code', 'todo_description' : 'try coding'},
# #             {'todo_id' : 3, 'todo_name' : 'work', 'todo_description' : 'try newjob'}]              

# all_todos = [Todo(todo_id=1, todo_name='gym', todo_description='try workout'),
#             Todo(todo_id=2, todo_name='code', todo_description='try coding'),
#             Todo(todo_id=3, todo_name='work', todo_description='try new job')]       


# @app.get("/alltodo", response_model=List[Todo])
# def get_all_todos():
#     return all_todos

# # GET a single todo by ID
# @app.get("/alltodo/{todo_id}", response_model=Todo)
# def get_todo(todo_id: int):
#     for todo in all_todos:
#         if todo.todo_id == todo_id:
#             return todo
#     raise HTTPException(status_code=404, detail="Todo not found")

# # POST a new todo
# @app.post("/alltodo", response_model=Todo)
# def add_todo(todo: Todo):
#     if any(existing.todo_id == todo.todo_id for existing in all_todos):
#         raise HTTPException(status_code=400, detail="Todo with this ID already exists")
#     all_todos.append(todo)
#     return todo

# # PUT (update) an existing todo
# @app.put("/alltodo/{todo_id}", response_model=Todo)
# def update_todo(todo_id: int, update: Update):
#     for todo in all_todos:
#         if todo.todo_id == todo_id:
#             if update.todo_name is not None:
#                 todo.todo_name = update.todo_name
#             if update.todo_description is not None:
#                 todo.todo_description = update.todo_description
#             return todo
#     raise HTTPException(status_code=404, detail="Todo not found")

# # DELETE a todo
# @app.delete("/alltodo/{todo_id}")
# def delete_todo(todo_id: int):
#     for index, todo in enumerate(all_todos):
#         if todo.todo_id == todo_id:
#             deleted = all_todos.pop(index)
#             return {"message": "Todo deleted", "todo": deleted}
#     raise HTTPException(status_code=404, detail="Todo not found")


# @app.post('/alltodo')
# def add_todo(todo: Todo):
#     new_id = max(t['todo_id'] for t in all_todos) + 1

#     new_todo = {
#         'todo_id': new_id,
#         'todo_name': todo.todo_name,
#         'todo_description': todo.todo_description
#     }

#     all_todos.append(new_todo)
#     return new_todo



# @app.delete('/alltodo/{todo_id}')
# def todo_delete(todo_id:int):
#     for index, todo in enumerate(all_todos):
#         if todo['todo_id'] == todo_id:
#             deleted = all_todos.pop(index)
#             return deleted, all_todos
#     return "Error, not found"

# @app.get('/')
# def index():
#     return {'message':'Hello API'}

# @app.get('/alltodo/{todo_id}')
# def printone_todo(todo_id:int):
#     for todo in all_todos:
#         if todo['todo_id'] == todo_id:
#             return todo

# @app.get('/alltodo')
# def printgiven_todos(todo_ids:int = None):
#     for todo in all_todos:
#         if todo['todo_id'] == todo_ids:
#             return all_todos[:todo_ids]

