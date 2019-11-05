import math #nec e s sary f o r square root func t i on

class NegativeNumberError(Exception):
    pass        
def squareRoot (number) :
    try:
        if number < 0 :
            raise NegativeNumberError
        else:
            print(math.sqrt(number))
    except NegativeNumberError:
        print("Square root of negative number not permitted")

squareRoot(16)
squareRoot(10)
squareRoot(-16)
squareRoot(9)


