import sqlite3
sqlite_path = 'db/sql_training.sqlite'
connection = sqlite3.connect(sqlite_path)
cursor = connection.cursor()

try:
    cursor.execute("DROP TABLE IF EXISTS sample")
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS sample ( id INTEGER PRIMARY KEY, name TEXT)")
    data = [
        (1, '佐藤'),
        (2, '田中'),
        (3, '伊藤'),
        (4, '渡辺'),
        (5, '湯本')
    ]
    cursor.executemany("INSERT INTO sample VALUES (?, ?)", data)

    data = [
        (2,),
        (3,),
        (4,),
        (5,)
    ]
    cursor.executemany("DELETE FROM sample WHERE id=?", data)

    # コミット
    connection.commit()

except sqlite3.Error as e:
    print("sqlite3.Error occured: ".e.args[0])

# 動作確認
cursor.execute('SELECT * FROM sample')
print(cursor.fetchall())

connection.close()
