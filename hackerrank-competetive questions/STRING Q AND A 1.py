#ACCEPT two int values from the user and return there products . if th eproduct is greater than 1000
#then return there sum..

def add(x,y):
    return x+y

def products(x,y):
    if x*y>1000:
       return add(x,y)
    else:
         return x*y
a=int(input("enter the first value"))
b=int(input("enter the second value"))
print(products(a,b))
