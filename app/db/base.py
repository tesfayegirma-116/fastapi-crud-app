from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base, DeclarativeMeta
from fastapi import Depends
from fastapi import HTTPException, status

from app.core.config import settings
# create a schema called fastapi_db
engine = create_engine(settings.database_url)

# create a sessionmaker object
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# create a base class for our models
Base: DeclarativeMeta = declarative_base()

# create a dependency to inject the database session into the endpoints


def get_db():
    try:
        db = SessionLocal()
        yield db
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e)
        )
    finally:
        db.close()
