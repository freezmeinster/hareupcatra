import base
import storage
import virtual_machine
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from ..config import get_config

engine = create_engine(get_config("server","db_url"), echo=True)
SessionBase = sessionmaker(bind=engine)

base.Base.metadata.create_all(engine)

def get_session():
    return SessionBase()
