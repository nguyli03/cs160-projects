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
        #node=TreeNode(newnode)
        self.left=newnode
    def getLeft(self):
        return self.left
    def setRight(self,newnode):
        #node=TreeNode(newnode)
        #node.right=self.right
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
    def postOrder(self):
        if self.left !=None:
            self.left.postOrder()
        if self.right!=None:
            self.right.postOrder()
        print(self.data)        
class BinaryTree:
    def __init__(self):
        self.root=None
    def setRoot(self,data):
        self.root=data
    def getRoot(self):
        return self.root
def main():
    root=TreeNode('LN')
    e=TreeNode('E')
    t=TreeNode('T')
    i=TreeNode('I')
    a=TreeNode('A')
    n=TreeNode('N')
    m=TreeNode('M')
    s=TreeNode('S')
    u=TreeNode('U')
    r=TreeNode('R')
    w=TreeNode('W')
    d=TreeNode('D')
    k=TreeNode('K')
    g=TreeNode('G')
    o=TreeNode('O')
    h=TreeNode('H')
    v=TreeNode('V')
    f=TreeNode('F')
    l=TreeNode('L')
    p=TreeNode('P')
    j=TreeNode('J')
    b=TreeNode('B')
    x=TreeNode('X')
    c=TreeNode('C')
    y=TreeNode('Y')
    z=TreeNode('Z')
    q=TreeNode('Q')
    slash=TreeNode('/')
    
    root.setLeft(e)
    root.setRight(t)
    e.setLeft(i)
    e.setRight(a)
    i.setLeft(s)
    i.setRight(u)
    a.setLeft(r)
    a.setRight(w)
    s.setLeft(h)
    s.setRight(v)
    u.setLeft(u)
    r.setLeft(l)
    w.setLeft(p)
    w.setRight(j)
    t.setLeft(n)
    t.setRight(m)
    n.setLeft(d)
    n.setRight(k)
    m.setLeft(g)
    m.setRight(o)
    d.setLeft(b)
    d.setRight(x)
    k.setLeft(c)
    c.setRight(y)
    g.setLeft(z)
    g.setRight(q)    
    x.setLeft(slash)
    tree=BinaryTree()
    tree.setRoot(root)
    #print(tree.getRoot().getLeft().getData())
    #print(tree.getRoot().getRight().getData())
    #tree.getRoot().postOrderRight()
    #tree.getRoot().postOrderLeft()
    #d.postOrder()
    #m.postOrder()
    #print(tree.getRoot().getData())
    '''root1=TreeNode('$')
    current=root1
    file=open('morse.txt','r')
    line=file.readline()
    index=0
    while line!='':
        while index<len(line):
            if line[index]=='-':
                node=TreeNode('')
                current.setRight(node)
                current=current.getRight()
            if line[index]=='.':
                node=TreeNode('')
                current.setLeft(node)
                current=current.getLeft()
            if line[index]==' ':
                current.setData(line[index+1])
            index+=1
        line=file.readline()
    tree1=BinaryTree()
    tree1.setRoot(root1)'''
        
    
    file=open('message.txt','r')
    code=file.readline()
    
    answer=''
    
    while code!='':   
        current=tree.getRoot()
        index=0
        while index<len(code):
            if code[index]=='-':
                current=current.getRight()
            elif code[index]=='.':
                current=current.getLeft()
            elif code[index]==' ':
                answer=answer+str(current.getData())
                current=tree.getRoot()
            index+=1
        answer=answer+str(current.getData())
        code=file.readline()
        
    print(answer)    
if __name__=='__main__':
    main()