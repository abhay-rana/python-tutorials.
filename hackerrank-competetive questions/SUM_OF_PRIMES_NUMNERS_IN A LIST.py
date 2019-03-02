l1=[]
s=0
def sumprimes(l):
    for e in l:
        if e>1:
            for i in range(2, e):
                if e % i != 0:
                    pass
                else:
                    break
            else:                            ## else is called the no break statement
                l1.append(e)
                s=0
                for e in l1:
                    s = s + e
    print(l1)
    print(s)
sumprimes([1,5,6,-1,11,13])
