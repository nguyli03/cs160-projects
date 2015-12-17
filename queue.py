#Name: Linh Nguyen
#Class: CS160A
#Professor: D. Ranum

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    def getData(self):
        return self.data
    def getNext(self):
        return self.next
    def setData(self,newdata):
        self.data=newdata
    def setNext(self,newnext):
        self.next=newnext

class Queue:
    def __init__(self):
        self.head=None
   
    def enqueue(self,item):
        node=Node(item)
        current=self.head
        if current==None:
            self.head=node
        else:
            while current.getNext()!=None:
                current=current.getNext()
            current.setNext(node)
                
    def dequeue(self):
        current=self.head
        data=current.getData()
        self.head=current.getNext()
        return data     
            
    
    def size(self):
        count=0
        current=self.head
        while current!=None:
            count+=1
            current=current.getNext()
        return count
    def isEmpty(self):
        return self.head==None
    def front(self):
        current=self.head
        return str('The queue start at: ')+ str(current.getData())
    def __str__(self):
        current=self.head
        astr='['
        if current==None:
            astr+=']'
        else:
            while current!=None:
                temp=current.getData()
                current=current.getNext()
                astr=astr+str(temp)
                if current!=None:
                    astr+=','
            astr+=']'
        return astr    
    
def main():
    a=Queue()
    a.enqueue(2)
    a.enqueue(5)
    a.enqueue('dog')
    print(a.size())
    a.enqueue('math')
    print(a.size())
    print(a.front())
    print(a.dequeue())
    print(a.size())
    print(a.isEmpty())
    print(a.front())
    print(a)
    
if __name__=="__main__":
    main()
    