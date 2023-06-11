from sqlalchemy.orm import Session
from app.models.product import Product
from app.schemas.product import ProductCreate
from uuid import uuid4


def get_products(db: Session):
    return db.query(Product).all()


def create_product(db: Session, product: ProductCreate):
    product_data = product.dict()

    db_product = Product(id=uuid4(), **product_data)
    db.add(db_product)
    db.commit()
    db.refresh(db_product)

    return db_product
