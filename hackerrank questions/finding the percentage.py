n=int(input())
d={}
for e in range(n):
    s=input().split(" ")
    name=s[0]
    m1=float(s[1])
    m2=float(s[2])
    m3=float(s[3])
    d[name]=(m1,m2,m3)
print(d)
n=input("enter name")
x=d.get(n)
print(x)
add=0
for e in x:
    add=add+e
print(add/3)


