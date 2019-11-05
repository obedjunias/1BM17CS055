import math #ne c e s sary f o r square root func t i on

class exc(Exception):
    pass

class AgeExcep(exc):
    pass
    '''
    msg1=" "
    def __init__(self,msg):
        #print(msg)
        msg1=msg
        #print(msg1)
        '''
    def __str__(self):
        print("No negatives")
     

class agecheck:
    age = 1
        
    def setage (self) :
        try:
            age=int(input("Enter your age:"))
            if age < 0 :
                print("Wrong entry:")
                raise AgeExcep
            else:
                print("Correct entry:",age)
        except AgeExcep:
                print("Negative age not allowed")
                
ac=agecheck()
ac.setage()



