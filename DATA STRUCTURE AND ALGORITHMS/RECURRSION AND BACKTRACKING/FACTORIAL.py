#factorial of  a number using recurrsion

# def facto(n):
#     if n==1:
#         return 1
#     else:
#         return n*facto(n-1)
#
# x=int(input(""))
# print(facto(x))

## factorial of a number without recurrsion

n=int(input("enter"))
fact=1
for e in range(n,0,-1): #till the condition is true
    fact=fact*e
print(fact)
