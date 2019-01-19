#we have to enhance the functionality of the function by
#the decorator function
#in which we have to give the distinction to the student
def decor_function(any_function):
    def wrapper_function(marks):
        for e in marks:
            if e>=75:
                print("congrats")
        else:
            return any_function(marks)
    return wrapper_function

@decor_function
def result(marks):
    for e in marks:
        if e>=33:
            pass
        else:
            print("fail")
            break
    else:
        print("pass")

result([33,75,80,23,55])

# n=int(input("how many marks do you want to enter"))
# marks=[]
# for e in range(n):
#     l=int(input())
#     marks.append(l)
# result(marks)
