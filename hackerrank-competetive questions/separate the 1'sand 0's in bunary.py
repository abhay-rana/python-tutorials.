l=[int(x) for x in input()]
print(l)
l.sort()
l1=[]
for e in l:
    if e==1:
        l1.append(e)
    elif e==0:
        l1.append(e)
    else:
        pass

l=l1[::-1]
print(l)
for e in l:
    print(e,end='')
