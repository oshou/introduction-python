import sqlite3
import memcache

db = memcache.Client(['127.0.0.1:11211'])

conn = sqlite3.connect('test_sqlite2.db')
curs = conn.cursor()

def get_employ_id(name):
  employ_id = db.get(name)
  if employ_id:
    return employ_id
  curs.execute()
