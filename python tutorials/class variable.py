class student():
    clg="ignou" #class variable
    def __init__(self,name,roll_no):
        self.name=name
        self.roll_no=roll_no

    def display(self):
        print(self.name)
        print(self.roll_no)
        print(self.clg)


s1=student("abhay",1868433)
s1.display()

s2=student("satish",1258265)
s2.clg="dav"
s2.display()

s3=student("aditi",12545465)
s3.display()

student.clg="dav"
s4=student("shivam",454143453)
s4.display()

