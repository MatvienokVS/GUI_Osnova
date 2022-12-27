import sqlite3


def con():
    try:
        con = sqlite3.connect('datebase.bd')
        cursor = con.cursor()
        print('Подключен к SQLite datebase БДДС реф')
    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    # finally:
    #    if (con):
    #        con.close()
    #        print("Соединение с SQLite закрыто")


con()
