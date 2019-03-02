import sqlite3
sqlite_path = 'db/sql_training.sqlite'
connection = sqlite3.connect(sqlite_path)
cursor = connection.cursor()

try:
    cursor.execute('DROP TABLE IF EXISTS sample')
    # テーブル作成
    cursor.execute(
        'CREATE TABLE IF NOT EXISTS sample (id INTEGER PRIMARY KEY, name TEXT)')
    # データ投入
    cursor.execute("INSERT INTO sample values (1, '佐藤')")
    cursor.execute("INSERT INTO sample values (?, ?)", (2, '田中'))

    # データ投入(複数件)
    data = [
        (3, '伊藤'),
        (4, '渡辺'),
        (5, '湯本')
    ]
    cursor.executemany("INSERT INTO sample values (?,?)", data)

    # コミット
    connection.commit()
except sqlite3.Error as e:
    print('sqlite3.Error occured: ', e.args[0])

# 動作確認
cursor.execute('SELECT * FROM sample')
print(cursor.fetchall())

connection.close()
