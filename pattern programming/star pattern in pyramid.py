#row is enter by the user
#we have to make a star pattern in triangular shape or pyramid shape

n=int(input("enter the number of rows"))
for e in range(0,n):
    for j in range(0,n-e-1):
        print(end=" ")
    for j in range(0,e+1):
        print("*",end=" ")
    print()