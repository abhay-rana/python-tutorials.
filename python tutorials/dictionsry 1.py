#dictrionary is a data structure in python
#which do mapping with key and value

#firstly we make a empty dictionary
d={}
print("empty dictionary is ",d)
print(dict())

#dictionary with key and value
#key as a integer and value as a "string"

d={1:"you",2:"are",3:"awesome"}
print("\n dictionary with key and value")
print(d)

#dictoinary with mixed valule
d={"name":"abhay",1:[1,2,3,4],2:(5,6,7,8)}
print("\ndictionary with mixed value\n",d)

#dictionary created with dict()
d=dict({1:"you",2:"are",3:"awesome"})
print("\n dictionary created with dict()\n",d)

#dictionary created with each value as a pair
d=dict([(1,"you"),(2,"are"),(3,"abhay")])
print("\n dictionary created with each value as a pair\n",d)

#creating a nested dictionary
d={1:"you",2:"are",3:{1:"my",2:"name",3:"is",4:"abhay"}}
print("\n a nested dictionary\n",d)


d.clear() #deleting the key and value from the dictionary
# make it like a new

#adding element to the dictionary
d={}
print("\ndictionary is empty",d)

d[1]="abhay"
d[0]="rana"
d[3]="great"
print("\n dictionary new\n",d)

#adding set of values to a single key
d[4]=4,5,6
print("\n dictionary\n",d)

#updating existing key in a dictionary
d[1]="aditi"
print("\n updated key value\n",d)

#add nested dictionary in dictionary
d[5]={"nested":{1:"this",2:"is",3:"nested"}}
print("\n new nested dictionary \n",d)

#accessing a elemnt in dictionary
print("\naccess by the key 1")
print(d[1])
print(d[5]) #print value of 5"th no key
print(d[5]["nested"]) #access nested key

#access value in dictionary by get method
print("\n acees by the get method")
print(d.get(1))

#crerated a new dictionory
print("\ninitialize a new dictrionary\n")

# Initial Dictionary
Dict = {5: 'Welcome', 6: 'To', 7: 'Geeks',
        'A': {1: 'Geeks', 2: 'For', 3: 'Geeks'},
        'B': {1: 'Geeks', 2: 'Life'}}
print("Initial Dictionary: ")
print(Dict)

# Deleting a Key value
del Dict[6]
print("\nDeleting a specific key: ")
print(Dict)

# Deleting a Key from
# Nested Dictionary
del Dict['A'][2]
print("\nDeleting a key from Nested Dictionary: ")
print(Dict)

# Deleting a Key
# using pop()
Dict.pop(5)
print("\nPopping specific element: ")
print(Dict)

# Deleting a Key
# using popitem()
x=Dict.popitem()
print("\nPops first element: ")
print(Dict)
print("\n the pop item is\n",x)

# Deleting entire Dictionary
Dict.clear()
print("\nDeleting Entire Dictionary: ")
print(Dict)