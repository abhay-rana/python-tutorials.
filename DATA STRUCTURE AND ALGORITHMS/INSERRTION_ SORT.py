#INSERTION SORT IS SIMILAR TO E WE PLAYING CARDS
# THE WAY WE SORT THE CARDS

def insertion_sort(arr):
    for e in range(1,len(arr)):
        temp=arr[e]
        j=e-1
        while j>=0 and temp<arr[j]:
            arr[j+1]=arr[j]      # we are forwarding the elements
            j=j-1
        else:
            arr[j+1]=temp
    return arr


arr=[40,55,33,20,35,1,5]
print(insertion_sort(arr))