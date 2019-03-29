#WE SELECT THE SMALLEST VALUE IN THE LIST
#SWAP THE SMALLEST ELEMT WITH THE FIRST VALUE OF THE LIST
#AGAIN DO THIS PROCESS
#KEEP DOING THIS N-1 IMES TO PLACE ALL N VALUES IN THE SORT

def selection_sort(l):
    for i in range(len(l)):
        min_index=i
        for j in range(i+1,len(l)):
            if l[min_index]>l[j]:
                min_index=j

        l[i],l[min_index]=l[min_index],l[i]
    return l
l=[64,25,12,22,11,-1,0,1,5,4]
print(selection_sort(l))


