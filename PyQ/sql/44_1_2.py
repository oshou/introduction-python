import sqlite3
sqlite_path = 'db/sql_training.sqlite'
connection = sqlite3.connect(sqlite_path)
cursor = connection.cursor()

# 一度進めたカーソルは戻らない
cursor.execute('SELECT * FROM users')
print(cursor.fetchall())

print(cursor.fetchone())


# もう一度SELECT実行すると戻る
cursor.execute('SELECT * FROM users')
print(cursor.fetchone())
print(cursor.fetchone())
print(cursor.fetchone())
print(cursor.fetchone())
