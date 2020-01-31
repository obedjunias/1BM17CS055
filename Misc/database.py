import sqlite3
from employee import Employee

conn = sqlite3.connect('database.db')

c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS employees (
            id integer PRIMARY KEY,
            first varchar(10),
            last varchar(10),
            pay integer
            )""")


def insert(emp):
    with conn:
        c.execute("INSERT INTO employees VALUES (?,?,?,?)", (emp.empid,emp.fname,emp.lname,emp.pay))


def get_employee(lastname):
    c.execute("SELECT * FROM employees")
    return c.fetchall()


def update_salary(emp, pay):
    with conn:
        c.execute("""UPDATE employees SET pay = :pay
                    WHERE id = :id AND last = :last""",
                  {'id': emp.empid, 'last': emp.lname, 'pay': pay})


def remove_employee(emp):
    with conn:
        c.execute("DELETE from employees WHERE id = :id",
                  {'id': emp.empid})

emp_1 = Employee('Obed', 'Junias', 120000)
emp_2 = Employee('Abc', 'Def', 60000)



t1 = (12,'a','b',15)
t2 = (16,'c','d',56)


c.executemany("INSERT INTO employees VALUES (?,?,?,?)",(t1,t2))
employees = get_employee('Junias')
print(employees)

update_salary(emp_2, 95000)
remove_employee(emp_1)

employees = get_employee('Def')
print(employees)

conn.close()