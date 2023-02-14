from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from starlette import status

from database import get_db
from typing import List

#from models import Item

"""
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from starlette import status

from database import get_db
from domain.question import question_schema, 
"""

from domain.item import item_schema, item_crud

router = APIRouter(
    prefix="/api/item",
)


# @router.get("/list")
# def item_list():
#     db = SessionLocal()
#     _item_list = db.query(Item).order_by(Item.create_date.desc()).all()
#     db.close()
#     return _item_list

# @router.post("/create/", response_model=Item)
# async def item_insert(item:Item) -> Any:
#     db = SessionLocal()
#     db.add(Item)
#     db.commit()
#     db.close()
#     return item


#@router.get("/list", response_model=list[item_schema.Item])
@router.get("/list", response_model=List[item_schema.Item])
def item_list(db: Session = Depends(get_db)):
    _item_list = item_crud.get_item_list(db)
    return _item_list


@router.get("/detail/{item_id}", response_model=item_schema.Item)
def item_detail(item_id: int, db: Session = Depends(get_db)):
    item = item_crud.get_item(db, item_id=item_id)
    return item


@router.post("/create", status_code=status.HTTP_204_NO_CONTENT)
def item_create(_item_create: item_schema.ItemCreate,
                    db: Session = Depends(get_db)):
    item_crud.create_item(db=db, item_create=_item_create)