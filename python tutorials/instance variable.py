#there are 3 methods for defining the class
#1--> init()
#2--> method(function)
#3-->outside the class

#instance variable are unique
#all information are different for different users

class account():
    def __init__(self,acc_no,balance):
        self.ac=acc_no
        self.ba=balance
    def func(self,acc_no,balance):
        self.ac=acc_no
        self.ba=balance

a1=account(8882128301,500)
a2=account(9311520820,600)
print(a1.__dict__)
a2.func(9311520820,600)
print(a2.ac)
a1.ac=7065388466
a1.ba=400
print(a1.ac)
print(a2.ba)