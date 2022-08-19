from fastapi import FastAPI
from app.v1.router.user_router import user_route, login_route
from app.v1.router.task_router import task_route
import uvicorn
import asyncio

app = FastAPI()

app.include_router(user_route)
app.include_router(login_route)
app.include_router(task_route)

@app.get('/')
def home():
    return {"message": "hello from the FastAPI project"}

async def main():
    config = uvicorn.Config(
        "main:app",
        port = 5000,
        reload = True
    )
    server = uvicorn.Server(config)
    await server.serve()

if __name__ == "__main__":
    asyncio.run(main())