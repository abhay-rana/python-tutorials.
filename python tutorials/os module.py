import os


#name of the operating system like -poxis,nt,java
print(os.name)

#get current working directory
print("\n",os.getcwd())
print(os.path.abspath('')) #print the absolute path

#list of files and folders in the directory
print("\n",os.listdir()) #os.listdir('filepath_here')

#change the current directory in python
os.chdir(r"D:\ubuntu codings")
print("\ndirectory is changed")
print(os.getcwd())

#now change the cwd to pycharm projects
os.chdir(r"C:\Users\abhay rana\PycharmProjects")
print("\n",os.getcwd())
x=os.getcwd()
for current_path,sub_folders,files in os.walk(x):
    print(f"current path is:{current_path}")
    print(f"sub_folders is:{sub_folders}")
    print(f"files is :{files}")
