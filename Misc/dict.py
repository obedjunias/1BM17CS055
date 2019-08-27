dict = {}
n = int(input("Enter the no. of entries: "))
for i in range(n):
    name = input("Enter Name: ")
    grade = float(input("Enter the Grade: "))
    dict.update({name:grade})
    
for name,grade in dict.items():
    if(grade>9.0):
        print(name,end=" ")
print()

