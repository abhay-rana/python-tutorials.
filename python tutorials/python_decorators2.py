def decor_function(any_function):
    def wrapper_function(*args,**kwargs):
        print("this is awesome function")
        return any_function(*args,**kwargs)
    return wrapper_function



@decor_function
def func1(a):
    print(f"the value of {a}")
@decor_function
def func2():
    print("this is a function 2")

func1(5)
func2()
