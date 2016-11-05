import arrow

import pymongo
from pymongo import MongoClient
import secrets.admin_secrets
import secrets.client_secrets
MONGO_CLIENT_URL = "mongodb://{}:{}@localhost:{}/{}".format(
    secrets.client_secrets.db_user,
    secrets.client_secrets.db_user_pw,
    secrets.admin_secrets.port, 
    secrets.client_secrets.db)

try: 
    dbclient = MongoClient(MONGO_CLIENT_URL)
    db = getattr(dbclient, secrets.client_secrets.db)
    collection = db.dated

except:
    print("Failure opening database.  Is Mongo running? Correct password?")
    sys.exit(1)

RECORD = { "type": "test_memo", 
       "date":  arrow.now().isoformat(),
       "text": "MEMO"
      }

def get_memos():
    """
    Returns all memos in the database, in a form that
    can be inserted directly in the 'session' object.
    """
    records = [ ]
    for record in collection.find({"type": "test_memo"}):
        record['date'] = arrow.get(record['date']).isoformat()
        records.append(record)
    return records 

def same(real, expected):
    print(real, expected, sep='\n')
    return real == expected

def test_insertion():
    collection.insert(RECORD)
    col = get_memos()
    assert same(col[0], RECORD)

def test_deletion():
    deleted = collection.delete_many(RECORD)
    print(deleted)
    assert deleted != 0

def test_empty():
    memos = get_memos()
    assert same(memos, [])