from fastapi import FastAPI
from app.api import product, customer

app = FastAPI()

app.include_router(product.router, prefix="/products", tags=["products"])
app.include_router(customer.router, prefix="/customers", tags=["customers"])


@app.get("/")
def read_root():
    return {"Hello": "PY"}
