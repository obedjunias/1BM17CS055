class CallDetails:
    def __init__(self):
        self.fNum = ""
        self.tNum = ""
        self.dur = ""
        self.typ = ""

    def getDetails(self,list_of_called_objects):
        self.fNum = list_of_called_objects[0]
        self.tNum = list_of_called_objects[1]
        self.dur =  list_of_called_objects[2]
        self.typ =  list_of_called_objects[3]
        self.putDetails()
    def putDetails(self):
        print(self.fNum.ljust(20),end=" ")
        print(self.tNum .ljust(20),end=" ")
        print(self.dur.ljust(20),end=" ")
        print(self.typ.rjust(20))
        


        

class Util:
    def __init__(self):
        self.list_of_class_objects = []
    
    def parse_customer(self,list_of_call_string):
        for i in range(len(list_of_call_string)):
            self.list_of_class_objects.append(CallDetails())
            lis = list_of_call_string[i].split(",")
            self.list_of_class_objects[i].getDetails(lis)


call1 = "9990000001,9330000001,23,STD"
call2 = "9990000002,9330000002,54,Local"
call3 = "9990000003,9330000003,6,ISD"

list_of_call_string=[call1,call2,call3]
print("From:".ljust(20),end=" ")
print("To:".ljust(20),end=" ")
print("Dur:".ljust(20),end=" ")
print("Type:".rjust(20))
Util().parse_customer(list_of_call_string)








    