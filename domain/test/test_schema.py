import datetime

from pydantic import BaseModel, validator


class Test(BaseModel):
    id: int
    data: str
    create_date: datetime.datetime

    class Config:
        orm_mode = True


class TestCreate(BaseModel):
    data: str

    @validator('data')
    def not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError('empty data not allowed')
        return v