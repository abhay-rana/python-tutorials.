#decorators are use to enhance the functionallity of the program

def decor_function(any_function):
    def wrapper_function():
        print("this is awesome function")
        return any_function()
    return wrapper_function


@decor_function
def func1():
    print("this is function 1")

@decor_function
def func2():
    print("this is function 2")

func1()
func2()
