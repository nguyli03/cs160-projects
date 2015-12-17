def selectionSort(aList):
    for i in range(len(aList)-1,-1,-1):
        positionofMax=0
        for j in range(0,i+1):
            if aList[j]>alist[positionofMax]:
                positionofMax=j
        temp=aList[positionofMax]
        aList[positionofMax]=aList[i]
        aList[i]=temp
    return aList

alist = [54,26,93,17,77,31,44,55,20]
selectionSort(alist)
print(alist)

            
        