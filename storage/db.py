from utils.db import Storage,get_session

session = get_session()

def add_storage(name):
    storage = Storage(
        name = name,
        uuid = 's2342'
    )
    session.add(storage)
    session.commit()