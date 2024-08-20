import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/Add/", description="Add two integers, a and b, and return the result.")
def add(a: int, b: int) -> int:
    """Add two integers."""
    return a + b
@app.get("/Substract/", description="Substract two integers, a and b, and return the result.")
def sub(a: int, b: int) -> int:
    """Substract two integers."""
    return a - b
@app.get("/Mutiply/",description="Mutiply two float, a and b, and return the result.")
def mutiply(a: float, b: float) -> float:
    """Mutiply two floates"""
    return a * b
@app.get("/Devide/",description="Divide two float, a and b, and return the result.")
def devide(a: float, b: float) -> float:
    """Devide two floates"""
    return a / b


@app.get("/Add_test/", description="Add two values and return the result. (Type annotations are not enforced.)")
def add_test(a: int, b: int):
    """Add two values without type annotations."""
    return a + b

@app.get("/", description="Root endpoint that returns a greeting message.")
async def root():
    """Return a hello world message."""
    return {"message": "Hello World"}

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8112)
