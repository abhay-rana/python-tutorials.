l1=[]
def is_primes(l):
    for i in range(2, l):
        if l%i != 0:
            pass
        else:
            break

    else:                            ## else is called the no break statement
        l1.append(l)
    print(l1)
is_primes(13)