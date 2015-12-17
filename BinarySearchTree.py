from queue import Queue
class TreeNode:
    def __init__(self,newitem):
        self.data=newitem
        self.left=None
        self.right=None
    def getData(self):
        return self.data
    def setData(self,data):
        self.data=data
    def setLeft(self,newnode):
        self.left=newnode
    def getLeft(self):
        return self.left
    def setRight(self,newnode):
        self.right=newnode
    def getRight(self):
        return self.right
    def postOrderLeft(self):
        if self.left !=None:
            self.left.postOrderLeft()
        print(self.data)
    def postOrderRight(self):
        if self.right !=None:
            self.right.postOrderRight()    
        print(self.data)
    def inOrder(self):
        if self.left !=None:
            self.left.inOrder()
        print(self.data)
        if self.right!=None:
            self.right.inOrder()
               
class BinarySearchTree:
    def __init__(self):
        self.root=None
    def setRoot(self,data):
        self.root=data
    def getRoot(self):
        return self.root
    def search(self,item):
        found=False
        c=self.root
        while c!=None and not found:
            if c.getData()==item:
                found=True
            elif c.getData()>item:
                c=c.getLeft()
            else:
                c=c.getRight()
        return found
    def add(self,item):
        node=TreeNode(item)
        c=self.root
        p=None
        while c!=None:
            if item>c.getData():
                p=c
                c=c.getRight()
            elif item<=c.getData():
                p=c
                c=c.getLeft()
        if p==None:
            self.root=node
        else:
            if item>p.getData():
                p.setRight(node)
            else:
                p.setLeft(node)
    def countNode(self,root):
        c=root
        if c==None:
            return 0
        if c!=None:
            return 1+self.countNode(c.getLeft())+self.countNode(c.getRight())

def count(treeroot,item):
    if treeroot==None:
        return 0
    elif treeroot.getData()==item:
        return 1+count(treeroot.getLeft(),item)+count(treeroot.getRight(),item)
    else:
        return count(treeroot.getLeft(),item)+count(treeroot.getRight(),item)

def levelBylevel(tree):
    nq=Queue()
    nq.enqueue(tree.getRoot())
    while not nq.isEmpty():
        n=nq.dequeue()
        if n!=None:
            print(n.getData())
            if n.getLeft()!=None:
                nq.enqueue(n.getLeft())
            if n.getRight()!=None:
                nq.enqueue(n.getRight())
def main():
    node=TreeNode(20)
    tree=BinarySearchTree()
    tree.setRoot(node)
    tree.add(10)
    tree.add(7)
    tree.add(50)
    tree.add(8)
    tree.add(33)
    tree.add(10)
    tree.add(9)
    tree.add(10)
    tree.getRoot().inOrder()
    print(tree.search(33))
    print(tree.search(1))
    print(count(tree.getRoot(),10))
    print(count(tree.getRoot(),5))
    print(tree.countNode(tree.getRoot()))
    levelBylevel(tree)
if __name__=='__main__':
    main()
    