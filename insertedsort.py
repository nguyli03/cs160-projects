def insertionSort(aList):
    for i in range(1,len(aList)):
        currentvalue=aList[i]
        position=i
        while currentvalue<aList[position-1] and position>0:
            aList[position]=aList[position-1]
            position-=1
        aList[position]=currentvalue
    return aList

alist = [54,26,93,17,77,31,44,55,20]
insertionSort(alist)
print(alist)