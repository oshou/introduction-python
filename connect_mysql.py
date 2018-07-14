# -*- coding: utf-8 -*-
import mysql.connector


def main():
    cnt = mysql.connector.connect(
            host='localhost',
            port='3306',
            db='sampledb',
            user='root',
            password='root',
            charset='utf8'
    )

    db = cnt.cursor(buffered=True)

    db.close()
    cnt.close()


if __main__ == '__main__':
    main()
