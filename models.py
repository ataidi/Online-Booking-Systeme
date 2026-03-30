from sqlalchemy import Column, Integer, String , Decimal
from connections import Base,
from  datetime input datetime


class online(Base):
    __tablename__="online_tbl"
    id=Column(Integer,primary_key=True,autoincrement=True)
    email=Column(String(100)nullable=false)
    location=Column(string(100)nullable=false)
    title=Column(String(100)nullable=false)
    phone=Column(string(100)nullable=false)
