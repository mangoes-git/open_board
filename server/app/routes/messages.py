from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

import app.schemas as schemas
import app.controller as crud
from app.routes.dependencies import get_db

router = APIRouter()


@router.post("/users/{user_id}/items/", response_model=schemas.Message)
def create_item_for_user(
    user_id: int, item: schemas.MessageCreate, db: Session = Depends(get_db)
):
    return crud.create_user_item(db=db, item=item, user_id=user_id)


@router.get("/items/", response_model=list[schemas.Message])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.get_items(db, skip=skip, limit=limit)
    return items
