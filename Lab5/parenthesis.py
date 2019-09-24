class Parentheses:
    def __init__(self):
        self.o_list = []
        self.c_list = []
    def procesString(self,s):
        for each in s:
            if each == "(" or each == "{" or each == "[":
                self.o_list.append(each)
            else:
                self.c_list.append(each)
        
        if len(self.o_list) != len(self.c_list):
            print(self.o_list)
            print(self.c_list)
            print("Invalid List...")
        else:
            for i in range(len(self.o_list)-1,0,-1):
                if self.o_list[i] == "(" and self.c_list[i] == ")":
                    self.o_list.pop()
                    self.c_list.pop()
                elif self.o_list[i] == "{" and self.c_list[i] == "}":
                    self.o_list.pop()
                    self.c_list.pop()
                elif self.o_list[i] == "[" and self.c_list[i] == "]":
                    self.o_list.pop()
                    self.c_list.pop()
                else:
                    pass

            if len(self.o_list) == len(self.c_list) and len(self.o_list) == 0:
                print("Valid...")
            else:
                print("InValid...")

c = Parentheses()
c.procesString("(){}")