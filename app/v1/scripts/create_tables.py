#from app.v1.model.user_model import Base
from app.v1.model.task_model import Base
from app.v1.utils.db import engine

def create_tables():
    #Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)