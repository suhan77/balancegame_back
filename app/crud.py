from sqlalchemy.orm import Session
from app import models, schemas
from sqlalchemy import String
from sqlalchemy import cast


def get_user_by_id(db: Session, user_id: str):
    return db.query(models.User).filter(models.User.id == cast(user_id, String)).first()


def create_user(db: Session, user: schemas.UserCreate):
    new_user = models.User(
        id=user.id,
        password=user.password,  # 실제로는 해시화 필요
        gender=user.gender,
        birth_year=user.birth_year,
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
