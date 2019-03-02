#factorial of  a number using recurrsion

def facto(n):
    if n==1:
        return 1
    else:
        return n*facto(n-1)

x=int(input(""))
print(facto(x))

## factorial of a number without recurrsion

n=int(input("enter"))
fact=1
while(n>0): #till the condition is true
    fact=fact*n
    n=n-1
print(fact)
