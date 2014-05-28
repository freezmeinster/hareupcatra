from utils.db.db import get_session
from utils.db.storage import Storage

session = get_session()

def add_storage(name):
    storage = Storage(
        name = name,
        uuid = 's2342'
    )
    session.add(storage)
    session.commit()