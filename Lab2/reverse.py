def reversestr(str1):
    lis = str1.split(" ")
    lis.reverse()
    print(lis)
    a2 = " "
    a=a2.join(lis)
    return (a)
def reversechar(str1):
    lis = str1.split(" ")
    a=""
    for each in lis:
        a+=each[::-1]
        a+= " "
    return (a)


st = input("Enter the string: ")
s=reversestr(st)
s1=reversechar(st)
print(s)
print(s1)