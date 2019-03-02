import sqlite3
sqlite_path = 'db/sql_training.sqlite'
connection = sqlite3.connect(sqlite_path, isolation_level='EXCLUSIVE')

try:
    cursor = connection.execute('SELECT count(*) FROM users')
    cnt = cursor.fetchone()
    print('cnt ->', cnt[0])

    for i in range(10):
        connection.execute(
            'INSERT INTO users (id,username) VALUES (?, ?)', (4, 'saburou'))
    raise ValueError("Rollback Test")

    connection.commit()

except ValueError:
    connection.rollback()
    cursor = connection.execute('SELECT count(*) FROM users')
    cnt = cursor.fetchone()
    print('cnt ->', cnt[0])

finally:
    connection.close()
