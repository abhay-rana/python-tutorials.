list1=[9,5,12,47,52,4]  #list
tuple1=(1,5,2,4,3,78,1,2,6) #tuple
d1={1:'c',2:'a',5:'b',4:"e",6:"d"} #dictionary

#we are sorting list ,tuple and dictionary by sorted() function it is inbuilt function
#sort() is inbuilt function in list which is use only for the list

print(sorted(list1))
print(sorted(list1,reverse=True))
print(sorted(tuple1))
print(sorted(d1))
print(sorted(d1.keys()))
print(sorted(d1.values()))
print(sorted(d1.items()))
print(sorted(d1.items(),key=lambda x:x[1]))
