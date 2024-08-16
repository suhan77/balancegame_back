from sqlalchemy.orm import Session
from app import schemas, crud
from fastapi import HTTPException

'''
Service(비즈니스 로직)를 만들 때에는 클래스로 만드는 것이 좋다.
이유는 관리 하기가 편하기 때문 이다.
'''


class UserService:
    @staticmethod
    def create_user(user: schemas.UserCreate, db: Session):
        db_user = crud.get_user_by_id(db, user_id=user.id)
        if db_user:
            raise HTTPException(status_code=400, detail="ID already registered")
        return crud.create_user(db=db, user=user)
