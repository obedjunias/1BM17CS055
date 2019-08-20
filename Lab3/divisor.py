def divisor(n):
    a=[]
    for i in range(1,n+1):
        if(n%i==0):
            a.append(i)
    for each in a:
        print(each,end=" ")
    print()

n=int(input("Enter the number: "))
divisor(n)