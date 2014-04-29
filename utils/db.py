from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
engine = create_engine('sqlite:///:memory:', echo=True)
SessionBase = sessionmaker(bind=engine)

class Switch(Base):
    __tablename__ = "switch"
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    uuid = Column(String)
    
    def __repr__(self):
        return self.name

class Storage(Base):
    __tablename__ = "storage"
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    uuid = Column(String)
    
    def __repr__(self):
        return self.name

class VirtualServer(Base):
    __tablename__ = "virtual_server"
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    uuid = Column(String)
    
    def __repr__(self):
        return self.name
    
Base.metadata.create_all(engine)

def get_session():
    return SessionBase()
