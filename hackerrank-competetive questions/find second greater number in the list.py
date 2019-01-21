
n=int(input())
l=list(map(int,input().strip().split()))
print(l)
l=l[:n]
print(l)
l=list(set(l))
l.sort()
print(l[-2])