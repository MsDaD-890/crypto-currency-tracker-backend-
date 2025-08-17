from fastapi import FastAPI
from src.router import router as router_crypto


app = FastAPI()

app.include_router(router_crypto)




    