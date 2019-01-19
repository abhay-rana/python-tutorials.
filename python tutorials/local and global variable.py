##local variable--> scope is limited to the inside a function
##global variable --> can be used through out the program


y=10  #global variable
def f1():
    x=5  #local variable
    print("inside variable",x)
    print("outside variable",y)

f1()
try:
    print("inside variable",x)
except NameError:
    print("see the scope is limited ")




def f2():
    global y #making a global variable inside the function
    y=5
    print("inside function",y)
f2()
print(y)



y=10
print("outside function",y)
def f3():
    y=5 #local variable
    print("inside function",y)
    print("outsdie function",globals()['y']) #using a global variable
f3()
print("outside function",y)

