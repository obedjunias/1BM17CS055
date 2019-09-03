class Student:
    def __init__(self):
        self.name = " "
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
        self.total = sum(self.cie) + sum(self.see)
        print("Topper is: ",self.name)
        print("Total: ",self.total)

# s1 = Student()
# s1.setdata()
# s1.display()
# s2 = Student()
# s2.setdata()
# s2.display()
s = []
n = int(input("Enter the number of students: "))
for i in range(n):
    s.append(Student())
    s[i].setdata()
maxx = 0
pos = 0
for i in range(n):
    if(s[i].total > maxx):
        maxx = s[i].total
        pos = i
    
print("*************************Topper Details**************************")
s[pos].display()






    