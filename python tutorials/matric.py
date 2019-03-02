# m=int(input("enter rows"))
# n=int(input("enter cloumns"))
# Matrix = [[int(input()) for x in range(n)] for y in range(m)]
# print(Matrix)
#
# for j in Matrix:
#     print(j)
#

#ANOTHER METHOD
m=int(input("enter rows"))
n=int(input("enter cloumns"))
mat=[]
for i in range(0,m):
    mat.append([])
for i in range(0,m):
    for j in range(0,n):
        mat[i].append(j)
        mat[i][j]=0
for i in range(0,m):
    for j in range(0,n):
        print("entry in row:",i+1,"column:",j+1)
        mat[i][j]=int(input())
print(mat)

#another method

m=int(input("enter rows"))
n=int(input("enter cloumns"))
mat=[]
for i in range(0,m):
    mat.append([])
for i in range(0,m):
    for j in range(0,n):
        x=int(input())
        mat[i].append(x)

print(mat)
