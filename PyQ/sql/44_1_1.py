import sqlite3
sqlite_path = 'db/sql_training.sqlite'

connection = sqlite3.connect(sqlite_path)

cursor = connection.cursor()
cursor.execute('SELECT * FROM users')

res = cursor.fetchall()
print(res)
connection.close()
