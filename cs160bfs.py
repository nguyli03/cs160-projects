from cs160graph import Graph
from cs160vertex import Vertex
from queue import Queue

def bfs(g,start):
  s = g.getVertex(start)
  s.setDistance(0)
  s.setPred(None)
  vertQueue = Queue()
  vertQueue.enqueue(s)
  while (vertQueue.size() > 0):        
    currentVert = vertQueue.dequeue()
    for nbr in currentVert.getConnections():          
      if (nbr.getColor() == 'white'):
        nbr.setColor('gray')
        nbr.setDistance(currentVert.getDistance() + 1)
        nbr.setPred(currentVert)
        vertQueue.enqueue(nbr)
    currentVert.setColor('black')

def main():
  g=Graph()
  g.addEdge('a','b')
  g.addEdge('b','a')
  g.addEdge('a','d')
  g.addEdge('d','a')
  g.addEdge('c','b',1)
  g.addEdge('b','c')
  g.addEdge('c','d')
  g.addEdge('d','c')
  bfs(g,'a')
  print(g.getVertex('c').getDistance())
  print(g.getVertex('c').getWeight(g.getVertex('b')))
  bfs(g,'c')
  print(g.getVertex('d').getDistance())
if __name__=='__main__':
  main()