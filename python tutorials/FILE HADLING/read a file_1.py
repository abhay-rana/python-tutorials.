#READ WRITE AND MANIPULATION WITH A FILE
# if the python file and text file in a same folder,OTHERWISE GIVE FULL PATH
#read method
#seek method
#open method
#clode method
#tell method
#read line method
#readlines method
#object.name---> to see the name of the file

#open() -->object=open(filepath,mode)
# f=open(r"file.txt",'r') #path of the file
# print(f.read())
# f.close()

#tell() --> tell about the position of the cursor

# f=open(r"file.txt",'r') #path of the file
# print(f.tell())
# print(f.read())
# print("cursor position",f.tell())
# print(f.read())
# f.close()

#seek() ---> change sthe position of the cursor

f=open(r"file.txt",'r') #path of the file
print(f.tell())
# print(f.read())
# print("cursor position",f.tell())
# print(f.read())
# f.seek(0)
# print(f.read())
# print("cursor position",f.tell())


#readline()
print(f.readline(),end='')#read and return only a single line
print(f.readline())


#readlines() give return of line in a list
f.seek(0)
print(f.readlines())

#to see the name of the file
print(f.name) #object.name

#to see the file is closed or not
#return on true or false

print(f.closed)

f.close()
print(f.closed)

#there are 7 modes in file handling
# 'r'
# 'w'
# 'a'
# 'r+'