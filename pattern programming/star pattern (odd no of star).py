#there is a star pattern
#row is enter by the user
#and there is odd no. of star in columns

n=int(input("enter the rows"))
k=1
for e in range(1,n+1):
   for i in range(1,k+1):
       print("*",end=" ")
   k=k+2
   print()
