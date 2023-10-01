# contains all the database schemas
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine, Column, Integer, String, Date
from dotenv import load_dotenv
import os

config = load_dotenv(".env")

Base = declarative_base()
posgresUrl = os.environ.get("POSGRESQL_URL")
engine = create_engine(posgresUrl)


class User(Base):
    __tablename__ = "User"
    # username consider as id
    id = Column(String, primary_key=True)
    name = Column(String(50), nullable=False)
    email = Column(String(255), nullable=False, unique=True)
    password = Column(String(255), nullable=False)
    DOB = Column(Date)
    age = Column(Integer)


class FollowShip(Base):
    # followers and following details
    __tablename__ = "Followship"
    id = Column(String, primary_key=True, autoincrement=True)
    followersId = relationship(User.id)
    followingId = relationship(User.id)


Base.metadata.create_all(engine)
engine.dispose()
