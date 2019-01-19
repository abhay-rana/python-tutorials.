# making a class by oops
# in python list,int,float all are inbuilt class
class Person():
    def __init__(self,first_name,last_name,age):
        self.first_namE=first_name
        self.last_name=last_name
        self.age=age


P1=Person("abhay","rana G",18) #object is created
P2=Person("aditi","rana",17)

print(P1.last_name)
print(P2.age)