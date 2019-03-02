## sort a dictionary according to the key

d={5:"a",3:"b",1:"c",4:"d",6:"e"}
#sorted according to the key
print(sorted(d,key=None,reverse=False))
#sorted according to the values
print(sorted(d.values()))
#sorted according to the items
print(sorted(d.items())) #sorted by the first element
#sorted according to the items
#sorted by the values
print(sorted(d.items(),key=lambda x:x[1]))
