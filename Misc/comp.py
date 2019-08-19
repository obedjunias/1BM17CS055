def comp(a,b):
    if(a>b):
        print(a," is greater than ",b)
    elif(a<b):
        print(a," is lesser than ",b)
    else:
        print(a," is equal to ",b)
ch = True
while ch:
    a = input("Enter Something: ")
    b = input("Enter Something: ")
    comp(a,b)
    ex = input("Want to exit-yes/no: ")
    if(ex == 'yes'):
        ch = False
    else:
        ch = True
