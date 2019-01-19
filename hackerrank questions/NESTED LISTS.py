
n=int(input())
scores=[]
for e in range(n):
    name=input()
    grades=float(input())
    scores.append([name,grades])

print(scores)
givengrades=set(x[1] for x in scores)
givengrades=list(givengrades)
givengrades.sort()
print(givengrades)
print(givengrades[1]) #it prints the second lowest
sts=sorted(x[0] for x in scores if x[1]==givengrades[1])  #the name is enter in this list
for s in sts:
    print(s)

