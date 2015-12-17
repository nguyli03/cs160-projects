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

class List:
    def __init__(self):
        self.head=None
    def isEmpty(self):
        return self.head==None
    def add(self,item):
        node=Node(item)
        node.setNext(self.head)
        self.head=node
    def length(self):
        node=self.head
        count=0
        while node!=None:
            count+=1
            node=node.getNext()
        return count
    def search(self,item):
        node=self.head
        found=False
        while node!=None and not found:
            if node.getData()==item:
                found=True
            else:
                node=node.getNext()
        return found
    def remove(self,item):
        node=self.head
        found=False
        previous=None
        while node!=None and not found:
            if node.getData()==item:
                found=True
            else:
                previous=node
                node=node.getNext()
        if previous==None:
            self.head=node.getNext()
        else:
            previous.getNext(node.getNext())
    def append(self,newitem):
        node=Node(newitem)
        current=self.head
        c=None
        while current!=None:
            c=current
            current=current.getNext()
        if c==None:
            self.head=node
        else:
            c.setNext(node)
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
    def pop(self):
        current=self.head
        previous=None
        while current.getNext()!=None:
            previous=current
            current=current.getNext()
        data=current.getData()
        previous.setNext(current.getNext)
        return data
    def index(self,item):
        current=self.head
        found=False
        index=0
        while current!=None and not found:
            if current.getData()==item:
                found=True
            else:
                current=current.getNext()
                index+=1
        return index
    def popat(self,pos):
        current=self.head
        previous=None
        index=0
        if pos==0:
            self.head=current.getNext()
        else:
            while index!=pos:
                index+=1
                previous=current
                current=current.getNext()
            data=current.getData()
            previous.setNext(current.getNext())
        return data
def main():
    L=List()
    L.add(5)
    L.add(6)
    print(L.search(2))
    print(L.length())
    L.add(7)
    print(L.search(6))
    L.append(9)
    print(L.search(9))
    print(L)
    print(L.pop())
    print(L.index(7))
    print(L.index(5))
    print(L.popat(2))
main()
            