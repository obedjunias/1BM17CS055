class Employee:
    Id = 0
    def __init__(self,fn,ln,p):
        Employee.Id = Employee.Id + 1
        self.empid = Employee.Id 
        self.fname = fn
        self.lname = ln
        self.pay = p

