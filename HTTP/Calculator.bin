import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/Add/")
def add(a: int, b: int) -> int:
    """Add two integers."""
    return a + b
@app.get("/Substract/")
def sub(a: int, b: int) -> int:
    """Substract two integers."""
    return a - b
@app.get("/Mutiply/")   
def mutiply(a: float, b: float) -> float:
    """Mutiply two floates"""
    return a * b
@app.get("/Devide/")
def devide(a: float, b: float) -> float:
    """Devide two floates"""
    return a / b


@app.get("/Add_test/")
def add_test(a, b):
    """Add two values without type annotations."""
    return a + b

@app.get("/")
async def root():
    """Return a hello world message."""
    return {"message": "Hello World"}

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8112)
