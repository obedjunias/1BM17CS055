from random import randint
import string

def password(str1,num):
     p = ""
     for i in range(num):
         p += str1[randint(1,100)]
     return p


str1 = string.printable
# for i in range(8):
#        print(str1[randint(1,100)],end="")
PC = password(str1,8)
print(PC)