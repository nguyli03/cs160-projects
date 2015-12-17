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
    root1=TreeNode('$')
    file=open('morse1.txt','r')
    line=file.readline().rstrip()
    while line!='':
        index=0
        current=root1
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
        line=file.readline().rstrip()

    tree1=BinaryTree()
    tree1.setRoot(root1)
    print(tree1.getRoot().postOrderLeft())
    
    '''file=open('message.txt','r')
    code=file.readline()
    current=tree1.getRoot()
    print(current.getData())
    answer=''
    index=0
    while code!='':   
        while index<len(code):
            if code[index]=='-':
                current=current.getRight()
            elif code[index]=='.':
                current=current.getLeft()
            elif code[index]==' ':
                string=current
                answer=answer+str(string.getData())
                current=tree.getRoot()
            index+=1
        answer=answer+str(current.getData())
        print(answer) '''
                
if __name__=='__main__':
    main()