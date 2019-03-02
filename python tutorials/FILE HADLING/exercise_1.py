#there is a file name is -- exercise 1 which is comma separated file
#this file contains a "name","salary"
#and u have to make a new file (updated) in which u have to write like this
# "name's" salary is "salary"

with open("exercise 1.txt",'r') as rf:
    with open("updated.txt",'w') as wf:
        for line in rf.readlines():
            name,salary=line.split(',')
            wf.write(f"{name}'s salary is {salary}")

f=open("updated.txt","r")
print(f.read())