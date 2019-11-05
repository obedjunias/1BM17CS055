
class superclass:
    def welc(self):
        print("Welcome to inheri in python")
    def setValue(self,x1):
        self.x1=x1
    def display(self):
        print("x1 in super",self.x1)
class subclass(superclass):
    def setValue(self,x2):
        self.x2=x2
    def display(self):
        print("x2 in sub",self.x2)

sup1=superclass()
sup1.welc()
sup1.setValue(100)
sup1.display()

sub1=subclass()
sub1.welc()
sub1.setValue(200)
sub1.display()
