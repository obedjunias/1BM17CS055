def isPrime(n):
    flag = True
    for i in range(2,n//2+1):
        if(n%i == 0):
            flag = False
            break
    return flag

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

for i in range(a,b+1):
    if(isPrime(i)):
        print(i,end=" ")
print()
    


