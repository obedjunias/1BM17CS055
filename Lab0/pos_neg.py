ch=True
while(ch):
    a = int(input("Enter first number: "))
    if(a>0):
        print("Number is positive")
    elif(a==0):
        print("Number is zero")
    else:
        print("Number is negative")
    ex = input("Want to exit-yes/no: ")
    if(ex == 'yes'):
        ch = False
    else:
        ch = True
