#print the star pattern in which the no.of rows is enter by the user

n=int(input("enter the rows"))
for e in range(1,n+1):
    for j in range(1,e+1):
        print("*",end=" ")
    print()
