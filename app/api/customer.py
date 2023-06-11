from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.customer import CustomerCreate, Customer
from app.api.crud.customer import get_customers, create_customer
from app.db.base import get_db

router = APIRouter()


@router.get("/", response_model=list[Customer])
def read_customers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    customers = get_customers(db, skip=skip, limit=limit)
    return customers


@router.post("/", response_model=Customer)
def create_new_customer(customer: CustomerCreate, db: Session = Depends(get_db)):
    return create_customer(db=db, customer=customer)
