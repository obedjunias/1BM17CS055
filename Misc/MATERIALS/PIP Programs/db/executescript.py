import sqlite3

con = sqlite3.connect("test4.db")
cur = con.cursor()
cur.executescript("""
    create table person1(
        firstname varchar(20),
        lastname varchar(20),
        age int
    );

    create table book1(
        title varchar(30),
        author varchar(20),
        published int
    );

    insert into book1(title, author, published)
    values (
        'Dirk Gently''s Holistic Detective Agency',
        'Douglas Adams',
        1987
    );
    """)
