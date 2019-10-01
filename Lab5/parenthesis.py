
class Parenthesis:
    def __init__(self):
        self.o_list=[]
        self.popped=None
    def isValid(self,str):
        valid=False
        for each in str:
            if each == '(' or each=='{' or each== '[':
                self.o_list.append(each)
            elif each == ')' or each=='}' or each== ']':
                if len(self.o_list) !=0 :
                    self.popped = self.o_list.pop()
                else:
                    self.popped=None
                if each == ')' and  self.popped == '(':
                    valid=True
                elif each == '}' and  self.popped=='{':
                    valid =True
                elif each == ']' and  self.popped =='[':
                    valid = True
                else:
                    valid =False
        if len(self.o_list) != 0:
            valid =False
        if(valid):
            print("Valid string...")
        else:
            print("Invalid String...")

str=input("Enter string")
Parenthesis().isValid(str)