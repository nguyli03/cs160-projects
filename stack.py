class Stack:
    def __init__(self):
        self.stack=[]
    def pop(self):
        return self.stack.pop()
    def push(self,item):
        self.stack.append(item)
    def peek(self):
        return self.stack[-1]
    def isEmpty(self):
        return len(self.stack)==0
    def size(self):
        return len(self.stack)
def main():
    s=Stack()
    s.push(1)
    s.push(5)
    s.push('dog')
    print(s.size())
    print(s.pop())
    print(s.peek())
    print(s.size())
    print(s.isEmpty())
if __name__=='__main__':
    main()