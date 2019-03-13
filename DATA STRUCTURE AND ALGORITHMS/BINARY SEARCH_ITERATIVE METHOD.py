# BINARY SEARCH USING ITERATIVE APPROACH
# BINARY SEARCH HAS ALSO HAVE A A MODULE IN PYTHON,
# WHICH CALLED BISECT METHOD
# remeber the list in sorted order

pos= -1       #THIS POSITION IS NOT EXIST
def binary_search(arr,x):
    low = 0
    upper = len(arr) - 1
    while low<=upper:
        mid = (low + upper) // 2
        if arr[mid] == x:
            globals()['pos']=mid+1   #definig the position of the elemnet globally
            return True  #if we got the element so stop and return the value
        elif arr[mid]<x:
            low=mid+1
        else:
            upper=mid-1

    return False

arr=[2,4,6,8,10]       #the sorted list
x=10       #the element which we have to search in the list
result=binary_search(arr,x)        #calling the binary search function
if result==True:
    print(f"yes,{pos}")
elif result==False:
    print("no")