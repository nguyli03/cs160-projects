import stack

def parChecker(symbolString):
    a=stack.Stack()
    balance =True
    
   
    i=0
    while i<len(symbolString) and balance:
        if symbolString[i]=='(':
            a.push(symbolString[i])
        else:
            if a.isEmpty():
                balance =False
            else:
                a.pop()
        i=i+1
    if a.isEmpty() and balance:
        return True
    else:
        return False
def main():
    print(parChecker('(((())'))
    print(parChecker('(())'))
if __name__=='__main__':
    main()
        