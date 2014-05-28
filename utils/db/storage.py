from base import Base
from sqlalchemy import Column, Integer, String


class Storage(Base):
    __tablename__ = "storage"
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    uuid = Column(String)
    
    def __repr__(self):
        return self.name