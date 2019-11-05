class MyError(Exception): 

    # Constructor or Initializer 
    def __init__(self, value): 
        self.value = value 
  
    # __str__ is to print() the value 
    def __str__(self): 
        return(str(self.value)) 
  
try: 
    raise(MyError("Wrong entry")) 
  
# Value of Exception is stored in error 
except MyError as error: 
    print('A New Exception occured: ',error) 

try:
    xx=MyError(100)
    raise(xx)
except MyError as error: 
    print('A New Exception occured: ',error.value) 
