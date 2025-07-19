from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import SessionLocal
from app.schemas.user import UserCreate, UserRead
from app.services.user import create_user, get_users

router = APIRouter(prefix="/users", tags=["Users"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=UserRead)
def create(user_in: UserCreate, db: Session = Depends(get_db())):
    return create_user(db, user_in)


@router.get("/{id}", response_model=List[UserRead])
def list_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_users(db, skip=skip, limit=limit)
