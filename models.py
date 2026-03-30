from sqlalchemy import Column, Integer, String,Float
from connections import Base
from  datetime import datetime
# modles
class Online(Base):
    __tablename__="online_tbl"
    id=Column(Integer,primary_key=True,autoincrement=True)
    email=Column(String(100),nullable=False)
    location=Column(String(100),nullable=False)
    title=Column(String(100),nullable=False)
    phone=Column(String(100),nullable=False)
