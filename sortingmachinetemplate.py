#Name: Linh Nguyen
#Class: CS160A
#Professor: D. Ranum

import random
import queue     #queue.py contains the class Queue

class RadixMachine:
    def __init__(self):
        self.mainBin = queue.Queue()
        self.DigitBin=[queue.Queue() for i in range(10)]

    def load(self, adeck):
        for i in adeck:
            self.mainBin.enqueue(i)
    def go(self):
        while self.mainBin.size()>0:
            x=int(self.mainBin.dequeue())
            self.DigitBin[x%10].enqueue(x)
        for i in range(0,10):
            while self.DigitBin[i].size()>0:
                x=self.DigitBin[i].dequeue()
                x=int(x)
                self.mainBin.enqueue(x)
        while self.mainBin.size()>0:
            x=self.mainBin.dequeue()
            x=int(x)
            self.DigitBin[(x%100)//10].enqueue(x)
        for i in range(0,10):
            while self.DigitBin[i].size()>0:
                x= self.DigitBin[i].dequeue()
                x=int(x)
                self.mainBin.enqueue(x)
        while self.mainBin.size()>0:
            x=self.mainBin.dequeue()
            x=int(x)
            self.DigitBin[x//100].enqueue(x)
        for i in range(0,10):
            while self.DigitBin[i].size()>0:
                x=self.DigitBin[i].dequeue()
                self.mainBin.enqueue(x)
    def unload(self):
        aList=[]
        while self.mainBin.size()>0:
            aList.append(self.mainBin.dequeue())
        return aList
    
def main(howmany):

    rm = RadixMachine()

    deck = []     #deck is a list
    for i in range(howmany):
        temp = random.randrange(1000)
        deck.append(temp)
    
    rm.load(deck)
    
    rm.go()
    
    sorteddeck = rm.unload()  #sorteddeck is a list
    
    for item in sorteddeck:
        print(item)

main(50)