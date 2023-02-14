from datetime import datetime

from domain.item.item_schema import ItemCreate
from models import Item
from sqlalchemy.orm import Session


def get_item_list(db: Session):
    item_list = db.query(Item).order_by(Item.create_date.desc()).all()
    return item_list


def get_item(db: Session, item_id: int):
    item = db.query(Item).get(item_id)
    return item


def create_item(db: Session, item_create: ItemCreate):
    db_item = Item(subject=item_create.subject,
                           content=item_create.content,
                           create_date=datetime.now())
    db.add(db_item)
    db.commit()