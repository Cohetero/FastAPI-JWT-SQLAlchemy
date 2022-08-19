from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'usuarios'

    id = Column(Integer(), primary_key = True)
    username = Column(String(50), nullable = False)
    email = Column(String(50), nullable = False, unique = True)
    password = Column(String(500), nullable = False)

    def __str__(self):
        return f"User (name={self.name}, email={self.email})"