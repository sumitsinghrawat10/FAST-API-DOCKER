from fastapi import FastAPI,Path,HTTPException
import json 

app=FastAPI()

def load_data():
    with open('news.json', 'r') as file:
        data = json.load(file)
    return data


@app.get("/")
def hello():
    return {"message": "Hello, World!"}


@app.get("/view")
def view():
    data = load_data()
    return data

@app.get("/data")
def get_status():
    data =load_data()

    f_data=[
        {"id":item["id"],"title":item["title"],"status":item["status"]} for item in data
    ]
    return f_data


@app.get("/status")
def views():
    data=load_data()

    resolved_count= [i for i in data if i["status"]=="Resolved"]

    return resolved_count

@app.get('/data/{id}')
def get_data_by_id(id:str=Path(...,description="Enter the id of the data to be fetched")):
    data=load_data()
    for item in data:
        if item["id"]==id:
            return item
    raise HTTPException(status_code=404, detail="Data not found")
