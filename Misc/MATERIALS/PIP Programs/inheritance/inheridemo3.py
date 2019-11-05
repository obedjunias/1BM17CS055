class superclass:
    #xx=10
    def welc(self):
        print("Welcome to inheri in python")
    def setValue(self,x1):
        self.x1=x1
        #xx=x1
    def display(self):
        print("x1 in super",self.x1)
        #print("xx in super",superclass.xx)
        #superclass.xx=3000
class subclass(superclass):
    def setValue(self,x2):
        superclass.setValue(self,1000)
        self.x2=x2
        #superclass.xx=800
    def display(self):
        superclass.display(self)
        print("x2 in sub",self.x2)
        #print("xx in sub",superclass.xx)
#print(superclass.xx)
sup1=superclass()
sup1.welc()
sup1.setValue(100)
sup1.display()
#print(superclass.xx)
sub1=subclass()
sub1.welc()
sub1.setValue(200)
sub1.display()
#print(superclass.xx)

