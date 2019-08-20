def search(li,a):
    if a in li:
        return True
    else:
        return False

n = int(input("Enter the number of elements to be inserted: "))
a=[]
print("Enter the numbers: ")
for i in range(n):
    num = int(input())
    a.append(num)
ele = int(input("Enter the elemnt to be searched: "))
if(search(a,ele)):
    print("Element Found")
else:
    print("Element Not Found")