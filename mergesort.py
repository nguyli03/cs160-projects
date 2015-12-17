def mergeSort(aList):
    if len(aList)>1:
        mid=len(aList)//2
        
        lefthalf=aList[:mid]
        righthalf=aList[mid:]
            
        mergeSort(lefthalf)
        mergeSort(righthalf)
        i=0
        j=0
        k=0
        while i<len(lefthalf) and j<len(righthalf):
            if lefthalf[i]<righthalf[j]:
                aList[k]=lefthalf[i]
                i+=1
                k+=1
            else:
                aList[k]=righthalf[j]
                j+=1
                k+=1
        if i < len(lefthalf):
            while i < len(lefthalf):
                aList[k]=lefthalf[i]
                i+=1
                k+=1
        if j < len(righthalf):
            while j<len(righthalf):
                aList[k]=righthalf[j]
                j+=1
                k+=1
    print (aList)
alist = [54,26,93,17,77,31,44,55,20]
mergeSort(alist)
print(alist)
