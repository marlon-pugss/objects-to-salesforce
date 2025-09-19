import os

import sqlalchemy as db
from sqlalchemy.orm import sessionmaker, declarative_base


db_debug_enabled = int(os.environ.get("DATABASE_DEBUG", "0"))
db_connection = os.getenv(
    "DATABASE_URL",
    "postgresql+psycopg://postgres:postgres@localhost:5432/leads",
)

Base = declarative_base()
BaseAudit = declarative_base()

engine = db.create_engine(
    db_connection,
    isolation_level="READ COMMITTED",
    echo=bool(db_debug_enabled),
)

session = sessionmaker(bind=engine, expire_on_commit=False)