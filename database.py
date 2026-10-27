import os
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

DB_URL = os.getenv("DATABASE_URL", "INVALID_URL")

ENGINE = create_engine(DB_URL, pool_pre_ping=True)
SESSION_LOCAL = sessionmaker(bind=ENGINE, autoflush=False)

class Base(DeclarativeBase):
    pass

def get_db():
    db = SESSION_LOCAL()
    try:
        yield db
    finally:
        db.close()
