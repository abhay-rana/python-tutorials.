#IN BUBBLE SORT WE JUST SWAP THE ADJACENT ELEMENT ]
# IF THE SECOND ELEMENT IS SMALLER THAN THE FIRST ELEMENT

def bubble_sort(arr):
    for i in range(len(arr)-1,0,-1):
        print()
        for j in range(i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j] #we are swapping
            print(arr)
    print()
    print("the final sorted array is ",arr)


arr=[10,2,3,5,1,8]
bubble_sort(arr)