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

def createDictionary(file,type2=None):
  dictionary={}
  file=open(file,'r')
  line=file.readline().rstrip()
  while line!='':
    line=line.split('|')
    if int(line[0]) in dictionary:
      if type2=='number':
        dictionary[int(line[0])].append(int(line[1]))
      else:
        dictionary[int(line[0])].append(line[1])
    else:
      if type2=='number':
        dictionary[int(line[0])]=[int(line[1])]
      else:
        dictionary[int(line[0])]=[line[1]]
    line=file.readline().rstrip()
  return dictionary  

def getMessage(g,vdata,edata,id):
  x=g.getVertex(id)
  message=vdata[id]
  y=x.getPred()
  while x.getPred()!=None:
    y=x.getPred()
    if y.getPred()!=None:
      message+= ' was in '+ edata[x.getWeight(g.getVertex(y.getId()))]+ \
      ' which also stared ' +vdata[x.getWeight(g.getVertex(y.getId()))]
    else:
      message+= edata[x.getWeight(g.getVertex(y.getId()))]
    x=y
  return message  
def main():
  '''movie=createDictionary('movies.txt')
  movieactor=createDictionary('movieactors.txt','number')
  actor=createDictionary('actors.txt')'''
  actor={}
  fileactor=open('actors.txt','r')
  line=fileactor.readline().rstrip()
  while line!='':
    line=line.split('|')
    actor[int(line[0])]=line[1]
    line=fileactor.readline().rstrip()
    
  movie={}
  filemovie=open('movies.txt','r')
  line2=filemovie.readline().rstrip()
  while line2!='':
    line2=line2.split('|')
    movie[int(line2[0])]=line2[1]
    line2=filemovie.readline().rstrip()
    
  movieactor={} 
  filemoact=open('movieactors.txt','r')
  line3=filemoact.readline().rstrip()
  while line3!='':
    line3=line3.split('|')
    if int(line3[0]) in movieactor:
      movieactor[int(line3[0])].append(int(line3[1]))
    else:
      movieactor[int(line3[0])]=[int(line3[1])]
    line3=filemoact.readline().rstrip()
    
  g=Graph()
  for key in actor.keys():
    g.addVertex(key)
  for key in movieactor.keys():
    for i1 in movieactor[key]:
      for i2 in movieactor[key]:
        if i1!=i2:
          g.addEdge(i1,i2,key)
  bfs(g,2)
  '''print(g.getVertex(7).getDistance())
  print(g.getVertex(7))
  print(movie[g.getVertex(7).getWeight(g.getVertex(1220))])'''
  print(g.getVertex(7))
  print(getMessage(g,actor,movie,7)+' which also stared '+ actor[2])
   
    
  name=input('Please enter an actor/actress name:')
  for key in actor.keys():
    if actor[key]==name:
      x=key
    else:
      x=0
  
  if x!=0:
    print(g.getVertex(x).getDistance())
  else:
    print('This actor/actress is not in database')

if __name__=='__main__':
  main()
  
    
    
  