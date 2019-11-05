import sqlite3

conn=sqlite3.connect('student.db')
cur=conn.cursor()
crea='''create table if not exists student(usn varchar(10),
      name varchar(25),cgpa float)'''
cur.execute(crea)
sel="select * from student"
dat=cur.execute(sel)

for x in dat:
    print("USN",x[0])
    print("Name",x[1])
    print("CGPA",x[2])

ins1='''insert into student values('1bm15cs020','aakash',8.5)'''
c1=cur.execute(ins1)
print("Record inserted")
sel="select * from student"
dat=cur.execute(sel)

for x in dat:
    print("USN",x[0])
    print("Name",x[1])
    print("CGPA",x[2])


'''
usn1=input()
nam1=input()
cgpa1=float(input())
print(usn1,nam1,cgpa1)'''
li=('1bm15cs001','xyz',9.7)
#li=[usn1,nam1,cgpa1]
ins3="insert into student values(?,?,?)"
c3=cur.execute(ins3,li)

sel="select * from student"
dat=cur.execute(sel)

for x in dat:
    print("USN",x[0])
    print("Name",x[1])
    print("CGPA",x[2])

data = [
('aa', 'bb', 9.1),
('aaa', 'bba', 9.2),
('bb', 'pqr', 8.2),
('bbb', 'xyz', 7.4), 
]
ins4="insert into student values(?,?,?)"
dat=cur.executemany(ins4,data)
print("After executemany");
sel="select * from student"
dat=cur.execute(sel)

for x in dat:
    print("USN",x[0])
    print("Name",x[1])
    print("CGPA",x[2])

    sql = '''select * from student'''
dat=cur.execute(sql)

dat1=cur.fetchone()
print("Fetching one record")
print(dat1)
'''
for x in dat1:
    print("USN",x[0])
    print("Name",x[1])
    print("CGPA",x[2])
'''
dat2=cur.fetchmany(2)
print("Fetching two record")
print(dat2)
li=list(dat2[0])
print(li[0])

dat3=cur.fetchall()
print (dat3)

print(conn.total_changes)

str="commit"
cur.execute(str)

str1="insert into student values('1BM12CS009', 'XYAAAA',8.7)"
co=cur.execute(str1)
print(co)
sel="select * from student"
dat=cur.execute(sel)
print("Before rollback")
for x in dat:
    print("USN",x[0])
    print("Name",x[1])
    print("CGPA",x[2])
conn.rollback()
sel="select * from student"
dat=cur.execute(sel)
print("After rollback")
for x in dat:
    print("USN",x[0])
    print("Name",x[1])
    print("CGPA",x[2])
conn.rollback()
