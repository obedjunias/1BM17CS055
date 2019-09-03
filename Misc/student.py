class Student:
    def __init__(self):
        self.cie = []
        self.see = []
        self.total = 0
    def setdata(self):
        self.name = input("Enter your Name: ")
        for i in range(3):
            self.cie.append(int(input("Enter your CIE mark: ")))
        for i in range(3):
            self.see.append(int(input("Enter your SEE mark: ")))
    def display(self):
        print("*************************Student Details**************************")
        self.total = sum(self.cie)/3 + sum(self.see)/3
        print("Total: ",self.total)

s1 = Student()
s1.setdata()
s1.display()
s2 = Student()
s2.setdata()
s2.display()
print("*************************Topper Details**************************")
if(s1.total > s2.total):
    print("Topper: ",s1.name)
else:
    print("Topper: ",s2.name)






    