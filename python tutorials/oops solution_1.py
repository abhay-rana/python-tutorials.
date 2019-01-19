
class Classy():
    fancy=0
    def __init__(self):
        self.items = []
    def addItem(self,things):
        if things=="tophat":
            Classy.fancy+=2
        elif things=="bowtie":
            Classy.fancy+=4
        elif things=="monocle":
            Classy.fancy+=5
        self.items.append(things)
    def getClassiness(self):
        return Classy.fancy

# Test cases
me =Classy()

# Should be 0
print(me.getClassiness())

me.addItem("tophat")
# Should be 2
print(me.getClassiness())

me.addItem("bowtie")
me.addItem("jacket")
me.addItem("monocle")
# Should be 11
print(me.getClassiness())

me.addItem("bowtie")
# Should be 15
print(me.getClassiness())

me.addItem("shoes")
#should be no change 0
print(me.getClassiness())
print("\n the list of items is")
print(me.items)
