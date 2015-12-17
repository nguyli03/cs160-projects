import stack
class Expression:
    def __init__(self,equation):
        self.equation=equation
    
    def __str__(self):
        return str(self.evaluate())        
    
    def evaluate(self):
        self.operands=stack.Stack()
        self.operators=stack.Stack()        
        pre={}
        pre['(']=1
        pre['+']=2
        pre['-']=2
        pre['*']=3
        pre['/']=3
        self.equation=self.equation.split()
        for i in self.equation:
            if i in "0123456789":
                self.operands.push(int(i))
            elif i=="(":
                self.operators.push(i)
            elif i==')':
                opp=self.operators.pop()
                while opp!='(':
                    opp2=self.operands.pop()
                    opp1=self.operands.pop()
                    x=self.doMath(opp,opp1,opp2)
                    self.operands.push(x)
                    opp=self.operators.pop()
            else: 
                while self.operators.size()>0 and \
                      (pre[self.operators.peek()]>=pre[i]) and \
                      self.operands.size()>=2:
                    opp=self.operators.pop()
                    opp2=self.operands.pop()
                    opp1=self.operands.pop()
                    self.operands.push(self.doMath(opp,opp1,opp2))
                self.operators.push(i)
        while self.operands.size()>1 and self.operators.size()>0:
            opp=self.operators.pop()
            opp2=self.operands.pop()
            opp1=self.operands.pop()
            x=self.doMath(opp,opp1,opp2)
            self.operands.push(x)
        return self.operands.pop()

    def doMath(self,opp,opp1,opp2):
        if opp=='+':
            return opp1+opp2
        if opp=='-':
            return opp1-opp2
        if opp=="*":
            return opp1*opp2
        if opp=="/":
            return opp1/opp2
def main():
    file=open('infix.txt','r')
    line=file.readline().rstrip()
    while line!="":
        result=Expression(line)
        print(line,' = ',result)
        line=file.readline().rstrip()
    file.close()
    
if __name__=='__main__':
    main()
                    
                    
            
                
        
            
            
            