def fib(n):
    if(n == 1):
        return 0
    elif( n == 2):
        return 1
    else:
        return fib(n-1)+fib(n-2)


a=int(input("Enter the no. :"))
l=[]
for i in range(1,a+1):
    l.append(fib(i))
for i in range(len(l)):
    print(l[i], end=" ")
print()
    