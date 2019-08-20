def even(l):
    el = []
    for each in l:
        if(each%2==0):
            el.append(each)
    print(el)

n = int(input("Enter the number of elements to be inserted: "))
a=[]
nl = []
print("Enter the numbers: ")
for i in range(n):
    num = int(input())
    a.append(num)
even(a)