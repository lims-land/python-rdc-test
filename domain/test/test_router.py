from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from starlette import status

from database import get_db
from typing import List

from domain.test import test_schema, test_crud

router = APIRouter(
    prefix="/api/test",
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
@router.get("/list", response_model=List[test_schema.Test])
def test_list(db: Session = Depends(get_db)):
    _test_list = test_crud.get_test_list(db)
    return _test_list


@router.get("/detail/{test_id}", response_model=test_schema.Test)
def test_detail(test_id: int, db: Session = Depends(get_db)):
    test = test_crud.get_test(db, test_id=test_id)
    return test


@router.post("/create", status_code=status.HTTP_204_NO_CONTENT)
def test_create(_test_create: test_schema.TestCreate,
                    db: Session = Depends(get_db)):
    test_crud.create_test(db=db, test_create=_test_create)