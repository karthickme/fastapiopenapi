from fastapi import FastAPI

app = FastAPI(
    title="FastAPI GitHub PR Demo",
    description="A demo FastAPI application with GitHub Actions for PR checks",
    version="0.1.0"
)

@app.get("/")
async def home():
    return {"message": "Hi"}

@app.get("/name/{name}")
async def greet_name(name: str):
    return {"message": f"Hi {name}"}

@app.get("/number/{number}")
async def greet_name(name: str):
    return {"Number is ": f"Hi {number}"}


if __name__ == "__main__":
    import uvicorn
    print("Just some print")
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
