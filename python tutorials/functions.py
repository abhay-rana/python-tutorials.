## there are 4 types of functions

#1--->takes something returns something
def add(a,b):
    add=a+b
    return add
x=add(3,4)
print("the sum is",x)

##2--> takes something returns nothing
def add(a,b):
    add=a+b
    print("sum is",add)
add(5,6)

##3--> takes nothing returns something

def multiply():
    a=int(input("enter"))
    b=int(input("enter"))
    return a*b

print("the multiply is ",multiply())

##4--> takes nothing returns nothing

def divide():
    a=int(input("enter"))
    b=int(input("enter"))
    x=a/b
    print("divison is ",x)

divide()