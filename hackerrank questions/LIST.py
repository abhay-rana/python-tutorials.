n = int(input())
l = []
for e in range(n):
    y = input().split(" ")
    x = y[0]
    if x == "insert":
        i = int(y[1])
        e = int(y[2])
        l.insert(i, e)
    elif x == "print":
        print(l)
    elif x == "pop":
        l.pop()
    elif x == "append":
        e = int(y[1])
        l.append(e)
    elif x == "remove":
        e = int(y[1])
        l.remove(e)
    elif x == "sort":
        l.sort()
    elif x == "reverse":
        l.reverse()

