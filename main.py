from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def say_hello():
    return {"message": "Hello world!"}


@app.get("/hello/{name}")
def say_hello_to_someone(name: str):
    return {"message": f"Hello {name}"}