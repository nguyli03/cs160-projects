class LogicGate:
    def __init__(self,n):
        self.label= n
        self.output= None
    def getLabel(self):
        return self.label
    def getOutput(self):
        self.output=self.performGateLogic()
        return self.output

class BinaryGate(LogicGate):
    def __init__(self,n):
        LogicGate.__init__(self,n)
        self.pinA=None
        self.pinB=None
    def getPinA(self):
        return int(input('Please enter pin A'))
    def getPinB(self):
        return int(input('Please enter pin B'))

class UnaryGate(LogicGate):
    def __init__(self,n):
        LogicGate.__init__(self,n)
        self.pinA=None
    def getPinA(self):
        return int(input('Please enter pin A'))

class AndGate(BinaryGate):
    def __init__(self,n):
        BinaryGate.__init__(self,n)
    def performGateLogic(self):
        a=self.getPinA
        b=self.getPinB
        if a==1 and b==1:
            return 1
        else:
            return 0

class OrGate(BinaryGate):
    def __init__(self,n):
        BinaryGate.__init__(self,n)
    def performGateLogic(self):
        a=self.getPinA()
        b=self.getPinB()
        if a==1 or b==1:
            return 1
        else:
            return 0

class NotGate(UnaryGate):
    def __init__(self,n):
        UnaryGate.__init__(self,n)
    def performGateLogic(self):
        a=self.getPinA
        if a==1:
            return 0
        else:
            return 1
'''
class Connector:
    def __init__(self,fgate,tgate):
        self.fgate=fgate
        self.tgate=tgate
        
        self.tonextPin(self)
    def getFrom(self):
        return self.fgate
    def getTo(self):
        return self.tgate
    def tonextPin(self):
        if self.pinA==None:
            self.pinA=source
        elif self.pinB==None:
            self.pinB=soure
        else:
            raise RuntimeError('No empty pin')
'''
def main():
    g1= OrGate('G1')
    print(g1.getOutput())
    print("hello")
   
    g2=AndGate("G2")
    g2.getOutput()
    
    g3=NotGate('G3')
    g3.getOutput()
main()
    
        