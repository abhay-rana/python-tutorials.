#make a decorator function in which
#it convert the lower case to the upper case
#withiout changing the original function

def high(func):
    def inner():
        s=func()
        print(s.upper())
        return func()
    return inner

@high
def low():
    return "good morning"

print(low())