from fastapi import FastAPI
from app.routers import boocks
 

app = FastAPI()
app.include_router(router=boocks.router)

