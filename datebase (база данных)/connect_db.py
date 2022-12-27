import sqlite3


def conn():
    with sqlite3.connect('datebase.bd') as db:
        print(('Подключен к базе данных'))


conn()
