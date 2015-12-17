'''Name: Linh Nguyen
   Class: CS160
   Professor: David Ranum
   Project: MorseTree'''

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
    def postOrder(self):
        if self.left !=None:
            self.left.postOrder()
        if self.right!=None:
            self.right.postOrder()
        print(self.data)        
class BinaryMorseTree:
    def __init__(self):
        self.root=None
    def setRoot(self,data):
        self.root=data
    def getRoot(self):
        return self.root
    def buildMorse(self,file):
        root=TreeNode('LN')
        self.root=root
        file=open(file,'r')
        line=file.readline().rstrip()
        while line!='':
            index=0
            current=self.root
            while index<len(line):
                if line[index]=='-':
                    if current.getRight()==None:
                        node=TreeNode('')
                        current.setRight(node)
                    current=current.getRight()
                if line[index]=='.':
                    if current.getLeft()==None:
                        node=TreeNode('')
                        current.setLeft(node)
                    current=current.getLeft()
                if line[index]==' ':
                    current.setData(line[index+1])
                index+=1
            line=file.readline().rstrip()
    def decode(self,code):
        answer=''
        current=self.root
        index=0
        while index<len(code):
            if code[index]=='-':
                current=current.getRight()
            elif code[index]=='.':
                current=current.getLeft()
            elif code[index]==' ':
                string=current
                answer=answer+str(string.getData())
                current=self.root                    
            index+=1
        answer=answer+str(current.getData())
        return(answer)       
def main():
    
    tree1=BinaryMorseTree()
    tree1.buildMorse('morse1.txt')
           
    '''print(tree1.getRoot().postOrderLeft())
    print(tree1.getRoot().postOrderRight())
    print(tree1.getRoot().getLeft().getLeft().postOrder())
    print(tree1.getRoot().getRight().getLeft().postOrder())'''
    print(tree1.getRoot().postOrder())
    
    
    file=open('message.txt','r')
    code=file.readline().rstrip()
    message=''
    while code!='':
        message+=tree1.decode(code)
        code=file.readline().rstrip()
    print(message)
if __name__=='__main__':
    main()