import sqlite3

conn = sqlite3.connect('facedb.db')
c = conn.cursor()

sql = """
CREATE TABLE Members (
  userid integer unique primary key autoincrement,
  username text,
  faceencode text
);
"""
c.executescript(sql)
conn.commit()

conn.close()
