from sqlalchemy.orm import Session
from app.models.customer import Customer
from app.schemas.customer import CustomerCreate
from uuid import uuid4


def get_customers(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Customer).offset(skip).limit(limit).all()


def create_customer(db: Session, customer: CustomerCreate):
    customer_data = customer.dict()

    db_customer = Customer(id=uuid4(), **customer_data)
    db.add(db_customer)
    db.commit()
    db.refresh(db_customer)

    return db_customer
