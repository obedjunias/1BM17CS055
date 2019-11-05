import math #ne c e s sary f o r square root func t i on
class NegativeNumberError ( ArithmeticError ) :
    """Attempted improper operat ion on ne gat i v e number
    . """
    pass
def squareRoot (number ) :
    """Computes square root of number . Raises NegativeNumberError if number is less than 0. """
    if number < 0 :
        raise(NegativeNumberError , "Square root of negative number not permitted")
    return math.sqrt (number)
try:
    print(squareRoot(10))
try:
    print(squareRoot(-3))
