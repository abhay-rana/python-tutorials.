l=[10,9,15,4,1,3,0,8]
e=0
while e<len(l)-1:
    min_val=l[e]
    for j in range(1,len(l)):
        if l[e]>l[j]:
            min_val=l[j]
            print(f"{e},{j},{min_val}")
            break
    e=j

print(min_val)

