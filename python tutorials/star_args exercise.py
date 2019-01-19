## define a function by the help of *args
#this function takes num and list of numbers
#this function prints the list of numbers but it takes the power of num ti the each number of the list

def power(num,*args):
   if len(l)==0:
        print("list is empty")
   else:
        return [i**num for i in args]
l=[1,2,3,4]
print(power(4,*l))