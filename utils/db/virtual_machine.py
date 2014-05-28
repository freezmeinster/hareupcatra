from base import Base
from sqlalchemy import Column, Integer, String

class VirtualServer(Base):
    __tablename__ = "virtual_server"
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    uuid = Column(String)
    
    def __repr__(self):
        return self.name