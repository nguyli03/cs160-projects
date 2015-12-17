class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.back=None
    def getData(self):
        return self.data
    def getNext(self):
        return self.next
    def getBack(self):
        return self.back
    def setData(self,newdata):
        self.data=newdata
    def setNext(self,newnext):
        self.next=newnext
    def setBack(self,newback):
        self.back=newback

class DoubleLinkedList:
    def __init__(self):
        self.head=None
    def isEmpty(self):
        return self.head==None
    def add(self,newitem):
        node=Node(newitem)
        current=self.head
        if current!=None:
            current.setBack(node)
            node.setNext(current)
            node.setBack(None)
            self.head=node
        else:
            self.head=node
    def length(self):
        count=0
        current=self.head
        if current==None:
            count=0
        else:
            while current!=None:
                count+=1
                current=current.getNext()
        return count
    def search(self,item):
        current=self.head
        found=False
        while current!=None and not found:
            if current.getData()==item:
                found=True
            current=current.getNext()
        return found
    def append(self,item):
        node=Node(item)
        current=self.head
        if current==None:
            self.head=node
        else:
            if current.getNext==None:
                current.setNext(node)
                node.setBack(current)
            else:
                while current.getNext()!=None:
                    current=current.getNext()
                   
                current.setNext(node)
                node.setBack(current)
            
    def pop(self):
        current=self.head
        while current.getNext()!=None:
            current=current.getNext()
        data=current.getData()
        p=current.getBack()
        p.setNext(None)
        return data
def main():
    L=DoubleLinkedList()
    L.add(5)
    L.add(6)
    L.add(7)
    print(L.isEmpty())
    print(L.length())
    L.append(8)
    L.append(9)
    print(L.length())
    print(L.pop())
    print(L.pop())
    print(L.length())
if __name__=="__main__":
    main()
        
        