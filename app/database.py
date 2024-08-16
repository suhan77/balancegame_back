from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session
# import os
# from dotenv import load_dotenv

# load_dotenv()
# DATABASE_URL = os.getenv("DATABASE_URL")
DATABASE_URL = "postgresql://jsh:1234@localhost:5432/postgres"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# 의존성 주입을 위한 DB 세션 함수
def get_db() -> Session:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
