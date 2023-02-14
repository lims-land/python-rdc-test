from sqlalchemy import Column, Integer, String, Text, DateTime
from database import Base

class Item(Base):
    __tablename__ = "item"

    id = Column(Integer, primary_key=True)
    subject = Column(String, nullable=False)
    content = Column(Text, nullable=False)
    create_date = Column(DateTime, nullable=False)


class Test(Base):
    __tablename__ = "test"

    id = Column(Integer, primary_key=True)
    data = Column(String, nullable=False)
    create_date = Column(DateTime, nullable=False)