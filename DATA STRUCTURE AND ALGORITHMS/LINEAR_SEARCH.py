#LINEAR SEARS JUST SIMPLY A SEARCH OF PARTICULAR ELEMT IN A SORTED OR A UNSORTED LIST

pos=-1
def linear_search(arr,x):
    for e in range(len(arr)):
        if arr[e]==x:
            globals()["pos"]=e+1
            return True
    else:
        return False


arr=[5,62,7,12,36,582,1]
x=7
result=linear_search(arr,x)
if result:
    print("element found at ",pos)
else:
    print("elemnt is not found")
