
def printPattern(n):
    for i in range(n):
        for j in range(n*(n-1)+1):
            if(j%n!=0 and j != n):
                print("-",end="")
            else:
                print(" ",end="")
        print('')
        if i != (n-1):
            for k in range(n*(n-1)+1):
                if k%n == 0:
                    print("|",end="")
                else:
                    print(" ",end="")
                
            print('')
n = int(input("Enter the size: "))
printPattern(n)
            