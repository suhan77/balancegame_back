from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import schemas
from app.database import get_db
from app.services.user_service import UserService

router = APIRouter()


@router.post("/signup/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return UserService.create_user(user=user, db=db)
