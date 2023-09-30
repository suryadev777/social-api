# contains all the database schemas
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, Integer, String, Date

Base = DeclarativeBase()


class User(Base):
    __tablename__ = "user"
    id = Column(String, primary_key=True)
    name = Column(String(50), nullable=False)
    email = Column(String(255), nullable=False, unique=True)
    password = Column(String(255), nullable=False)
    DOB = Column(Date)
    age = Column(Integer)
