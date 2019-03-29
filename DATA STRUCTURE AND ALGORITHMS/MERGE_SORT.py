#MERGE SORT ALGORITHMS CONCEPT
#IS BASED ON THE DIVIDE AND CONQUER
#IN THIS WE DIVIDE THE LIST INTO THE SUBLISTS

#method 1-->

def merge(left,right):
    result=[]
    i,j=0,0
    while i<len(left) and j<len(right):
        if (left[i])<=right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    result+=left[i:]
    result+=right[j:]

    return result

def mergesort(list):
    if len(list)<=1:
        return list

    mid=int(len(list))//2
    left=mergesort(list[:mid])
    right=mergesort(list[mid:])

    return merge(left,right)

arr=[33,35,40,20,21,1,2,5,4]
print(mergesort(arr))