t=int(input("enter"))
i=1
while i<=t:
    s=input()
    l=s.split()
    ss="not"
    if ss in l:
        print("real fancy")
    else:
        print("regular fancy")
        i+=1