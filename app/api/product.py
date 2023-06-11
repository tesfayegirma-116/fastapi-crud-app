from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.product import ProductCreate, Product
from app.api.crud.product import get_products, create_product as create_product_crud
from app.db.base import get_db

router = APIRouter()


@router.get("/", response_model=list[Product])
def read_products(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    products = get_products(db)
    return products


@router.post("/", response_model=Product)
def create_new_product(product: ProductCreate, db: Session = Depends(get_db)):
    return create_product_crud(db=db, product=product)
