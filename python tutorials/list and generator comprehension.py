squares=[i*i for i in range(1,5)]  #list comprehension
print(squares)
for e in squares:
    print(e)
for e in squares:
    print(e)


squares=(i*i for i in range(1,5))  #geneartor comprehension
print(squares)
for e in squares:
    print(e)
for e in squares:
    print(e)

squares=tuple(i*i for i in range(1,5))  #list comprehension
print(squares)
for e in squares:
    print(e)
for e in squares:
    print(e)

