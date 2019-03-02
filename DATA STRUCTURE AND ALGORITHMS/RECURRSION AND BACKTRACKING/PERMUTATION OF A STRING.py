def tostring(s):
    return ''.join(s)


def permutation(s,i,n):
    global count
    if i==n:   #if we are at the last element then ptint it
        count+=1
        return print(tostring(s),end=" "),print(f"{count}")
    else:
        for j in range(i,n+1):
            s[j],s[i]=(s[i],s[j]) #swapping
            permutation(s,i+1,n)  #recurrsion
            s[j],s[i]=(s[i],s[j])  #backtracking

count=0
s=list(input("enter a string"))
n=len(s)-1
permutation(s,0,n)