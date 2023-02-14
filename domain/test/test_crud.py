from datetime import datetime

from domain.test.test_schema import TestCreate
from models import Test
from sqlalchemy.orm import Session


def get_test_list(db: Session):
    test_list = db.query(Test).order_by(Test.create_date.desc()).all()
    return test_list


def get_test(db: Session, test_id: int):
    test = db.query(Test).get(test_id)
    return test


def create_test(db: Session, test_create: TestCreate):
    db_test = Test(data=test_create.data, create_date=datetime.now())
    db.add(db_test)
    db.commit()