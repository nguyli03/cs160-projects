import queue
def HotPotato(n,aList):
    aqueue=queue.Queue()
    for i in aList:
        aqueue.enqueue(i)
    while aqueue.size()>1:
        for i in range(n):
            aqueue.enqueue(aqueue.dequeue())
        aqueue.dequeue()
    return aqueue.dequeue()
def main():
    print(HotPotato(7,["Bill","David","Susan","Jane","Kent","Brad"]))
main()