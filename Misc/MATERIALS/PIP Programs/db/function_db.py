import sqlite3
from sqlite3 import Error

def create_conn(db_f):
    try:
        conn=sqlite3.connect(db_f)
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        conn.close()


if __name__ =='__main__':
    create_conn("F:\\python\db\pydb.db")
        
