class superclass:
    def welc(self):
        print("Welcome to inheri in python")
    def setValue(self,x1):
        self.x1=x1
    def display(self):
        print("x1 in super",self.x1)

try:
    from random import randint
    a=10
    print(a)
    b=20
    #b=0
    d1={"A":1,"B":2}

    c=a/b
    print(c)

    #print(d1["C"])
    print(d1["B"])

    yy=int(input("Enter a value:"))
    print(yy+10)
    
except NameError:
    print("Name not defined")
except KeyError:
    print("Key not seen")
except ZeroDivisionError:
    print("Denominator cannot be zero")
except ValueError:
    print("Value Missing for calculation")
    
except ImportError:
    print("File mentioned does not exist")
    
print("Hello welcome")

def f1(xx):
    if (xx<40):
        raise ValueError("Sorry you have not cleared")
try:
    a1 = int(input("Enter a positive integer: "))
    if a1 <= 0:
        raise ValueError("That is not a positive number!")
    f1(80)
    sup2=superclass()
    superclass.setValue(sup2,1000)
    sup2.display1()

except ValueError as ve:
     print(ve)
     
except AttributeError:
    print("Wrong attribute")
    
finally:
    print("leaving try now")

     
