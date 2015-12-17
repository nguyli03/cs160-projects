class BinaryHeap:
    def __init__(self):
        self.heapList=[0]*1000
    def add(self,item):
        #self.heapList.append(item)
        self.heapList[0]=self.heapList[0]+1
        self.heapList[self.heapList[0]]=item
        c=self.heapList[0]
        p=c//2
        while self.heapList[c]>self.heapList[p] and p>0:
            temp=self.heapList[c]
            self.heapList[c]=self.heapList[p]
            self.heapList[p]=temp
            c=p
            p=c//2
    def getMax(self):
        data=self.heapList[1]
        self.heapList[1]=self.heapList[self.heapList[0]]
        self.heapList[self.heapList[0]]=0
        self.heapList[0]=self.heapList[0]-1
        c=1
        cl=c+1
        cr=c+2
        while (cl<=self.heapList[0] or cr<=self.heapList[0]):
        #while self.heapList[0]>0:
            if self.heapList[cl]<self.heapList[cr]:
                if self.heapList[c]<self.heapList[cr] and cr<=self.heapList[0]:
                    temp=self.heapList[c]
                    self.heapList[c]=self.heapList[cr]
                    self.heapList[cr]=temp
                c=cr
                cl=cr*2
                cr=cl+1
            else:
                if self.heapList[c]<self.heapList[cl] and cl<=self.heapList[0]:
                    temp=self.heapList[c]
                    self.heapList[c]=self.heapList[cl]
                    self.heapList[cl]=temp
                c=cl
                cr=cl*2 
                cl=cr-1
        return data
def main():
    H=BinaryHeap()
    aList=[12,2,16,30,8,28,4,10,20,6]
    for i in aList:
        H.add(i)
    for i in range(0,10):
        print(H.getMax())
if __name__=='__main__':
    main()
    
        