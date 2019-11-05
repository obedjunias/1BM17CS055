class superclass:
    xx=[]
    def setValue(self,x1):
        self.xx.append(x1)
    def display(self):
        print("xx in super",self.xx)
        
class subclass(superclass):
    def setValue(self,x2):
        superclass.setValue(self,200)
        self.xx.append(x2)
        
    def display(self):
        superclass.display(self)
        print("xx in sub",self.xx)
print(superclass.xx)

sup1=superclass()
sup1.setValue(100)
sup1.display()

print(superclass.xx)

sub1=subclass()
sub1.setValue(300)
sub1.display()

print(superclass.xx)

