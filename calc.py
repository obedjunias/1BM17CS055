ch=True
while(ch):
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    c = input("Enter the operator: ")
    if(c=="+"):
        print(a+b)
    elif(c=='-'):
        print(a-b)
    elif(c=='*'):
        print(a*b)
    elif(c=='/'):
        if(b == 0):
            print("Division by zero")
        else:
            print(a/b)
    elif(c=='%'):
        if(b == 0):
            print("Division by zero")
        else:
            print(a%b)
    elif(c=='^'):
        print(a**b)
    else:
        print("Invalid Operator")
    ex = input("Want to exit-yes/no: ")
    if(ex == 'yes'):
        ch = False
    else:
        ch = True
