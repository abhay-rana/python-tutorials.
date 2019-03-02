from math import *
n=int(input("enter the test cases"))
l=[int(x) for x in input().split()]
print(l)
l1=[]
for e in l:
    l1.append(factorial(e))
print(l1)
l2=list(map(str,l1))
print(l2)
l3=[]
for e in l2:
    x=len(e)
    s=0
    for i in range(x):
        s=s+int(e[i])
    l3.append(s)
print(l3)


#
# from math import factorial
# n=int(input("enter the test cases"))
# l=[int(x) for x in input().split()]
# l=[factorial(e) for e in l]
# l=list(map(str,l))
# print(l)
# l2=[]
# for e in l:
#     x=len(e)
#     s=0
#     for i in range(x):
#         s=s+int(e[i])
#     l2.append(s)
# print(l2)