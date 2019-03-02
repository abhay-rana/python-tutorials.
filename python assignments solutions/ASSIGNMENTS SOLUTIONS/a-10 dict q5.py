#sum of values of dictionary
n=int(input("enter how many elements do you want to enter"))
d={}
for e in range(n):
    x=int(input("enter"))
    d[e]=x
print(d)
s=0
for v in d.values():
  s=s+v

print(s)
