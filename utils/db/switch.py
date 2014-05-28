from base import Base
from sqlalchemy import Column, Integer, String

class Switch(Base):
    __tablename__ = "switch"
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    uuid = Column(String)
    
    def __repr__(self):
        return self.name