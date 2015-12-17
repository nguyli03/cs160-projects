def quickSort(aList):
    quickSortHelper(aList,0,len(aList)-1)

def quickSortHelper(aList,start,end):
    if start<end:
        middle=partition(aList,start,end)
        quickSortHelper(aList,start,middle-1)
        quickSortHelper(aList,middle+1,end)
    
def partition(aList,start,end):
    initial=start
    leftmark=start+1
    rightmark=end
    done=False
    while not done:
        while aList[leftmark]<=aList[initial] and leftmark<=rightmark:
            leftmark+=1
        while aList[rightmark]>=aList[initial] and leftmark<=rightmark:
            rightmark-=1
        if leftmark>rightmark:
            done=True
        else:
            temp=aList[rightmark]
            aList[rightmark]=aList[leftmark]
            aList[leftmark]=temp
    temp=aList[rightmark]
    aList[rightmark]=aList[initial]
    aList[initial]=temp
    
    return rightmark


alist = [54,26,93,17,77,31,44,55,20]
quickSort(alist)
print(alist)