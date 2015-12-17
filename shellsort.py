def shellSort(aList):
    sublist=len(aList)//3
    while sublist>0:
        for start in range(sublist):
            sublistsort(aList,start,sublist)
        print('sort after having ', sublist,' is ',aList)
        sublist=sublist//3
    return aList
def sublistsort(aList,start,gap):
    for i in range(start+gap,len(aList),gap):
        currentvalue=aList[i]
        position=i
        while aList[position-gap]>currentvalue and position>=gap:
            aList[position]=aList[position-gap]
            position=position-gap
        aList[position]=currentvalue
alist = [54,26,93,17,77,31,44,55,20]
shellSort(alist)
print(alist)
            
            
        
    