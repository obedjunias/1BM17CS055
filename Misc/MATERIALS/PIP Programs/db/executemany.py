'''
import MySQLdb as my
 
db = my.connect(host="127.0.0.1",
user="root",
passwd="",
db="world"
)
'''
import sqlite3 
conn = sqlite3.connect('test1.db') 
cur=conn.cursor()
'''
name = "Some new city"
 
country_code = 'SNC'
 
district = 'Someyork'
 
population = 10008
 '''
data = [
('city 1', 'MAC', 'distrct 1', 16822),
('city 2', 'PSE', 'distrct 2', 15642),
('city 3', 'ZWE', 'distrct 3', 11642),
('city 4', 'USA', 'distrct 4', 14612),
('city 5', 'USA', 'distrct 5', 17672),
]

sql='''create table if not exists city( name varchar(20), countrycode varchar(5),
    district varchar(15),population int)'''
cur.execute(sql)
'''
sql = insert into city(name, countrycode, district, population) 
VALUES(%s, %s, %s, %d)
#cur.execute(sql)

number_of_rows = cur.executemany(sql, data)
'''
sql = '''select * from city'''
dat=cur.execute(sql)

dat1=dat.fetchone()
print(dat1)

db.commit()

 
db.close()
