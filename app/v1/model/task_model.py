from email.policy import default
from ssl import create_default_context
from sqlalchemy import ForeignKey, Column, Integer, String, BOOLEAN, DateTime
from sqlalchemy.orm import declarative_base, relationship
from .user_model import User
from datetime import datetime

Base = declarative_base()

class Task(Base):
    __tablename__ = 'tareas'

    id = Column(Integer(), primary_key = True)
    title = Column(String(100), nullable = False)
    create_at = Column(DateTime, default = datetime.now)
    is_done = Column(BOOLEAN, default = False)
    child_id = Column(Integer, ForeignKey(User.id))
    child = relationship(User)
