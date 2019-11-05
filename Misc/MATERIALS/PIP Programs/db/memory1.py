import sqlite3

def char_gen():
    import string
    for c in string.ascii_letters[:52]:
        yield(c,)

con=sqlite3.connect(":memory:")
cur=con.cursor()
#cur.execute("create table characters(c varchar(1))")

cur.executemany("insert into characters values(?)","3")#char_gen())

cur.execute("select c from characters")
print (cur.fetchall())

