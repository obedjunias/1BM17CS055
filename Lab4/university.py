class Student:
    id = 0
    def __init__(self):
        self.name = " "
        self.age = " "
        self.marks = 0
        Student.id += 1 
    def setdata(self):
        self.id_ = Student.id
        self.name = input("Enter your Name: ")
        self.age = int(input("Enter your age: "))
        self.marks = int(input("Enter your marks: "))
    def validate_marks(self):
        if(self.marks >= 0 and self.marks <= 100):
            return True
    def validate_age(self):
        if(self.age > 20):
            return True
    def check_qualification(self):
        if(self.validate_age() and self.validate_marks()):
            if(self.marks >= 65):
                return True
            else:
                return False
        else:
            return False
    def display(self):
        print("*************************Student Details**************************")
        if(self.check_qualification()):
            print("ID: ",self.id_)
            print("Name: ",self.name)
            print("Age: ",self.age)
            print("You are ELIGIBLE...")
        else:
            print("Sorry you are not eligible...")
    
s1 = Student()
s1.setdata()
s2 = Student()
s2.setdata()
s1.display()
s2.display()

