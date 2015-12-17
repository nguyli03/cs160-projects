'''Name: Linh Nguyen
Class: CS160
Professor: D.Ranum
Kevin Bacon game project'''

from cs160graph import Graph
from cs160vertex import Vertex
from queue import Queue
from cs160bfs import bfs
import sys

def createDictionary(file,key,value,typekey,typevalue,listvalue):
  dictionary={}
  file=open(file,'r')
  line=file.readline().rstrip()
  while line!='':
    line=line.split('|')
    if listvalue==True:
      if typekey(line[key]) in dictionary:
        dictionary[typekey(line[key])].append(typevalue(line[value]))
      else:
        dictionary[typekey(line[key])]=[typevalue(line[value])]
    else:
      dictionary[typekey(line[key])]=typevalue(line[value])
    line=file.readline().rstrip()
  return dictionary

def getMessage(g,vdata,edata,name,actorstart):
  x=g.getVertex(name)
  message=vdata[name]
  if x.getPred()==None:
    message+=' is not related to Kevin Bacon'
  else:
    while x.getPred()!=None:
      y=x.getPred()
      if y.getPred()!=None:
        message+= ' was in '+ edata[x.getWeight(y)]+ \
          ' which also stared\n' +vdata[y.getId()]
      else:
        message+='was in '+ edata[x.getWeight(y)]+'which aslo started '+actorstart
      x=y
  return message 


def buildGraph(vertecies,edges):
  g=Graph()
  for key in vertecies.keys():
    g.addVertex(key)
  for key in edges.keys():
    for i1 in edges[key]:
      for i2 in edges[key]:
        if i1!=i2:
          g.addEdge(i1,i2,key)
  return g

def main():
  movie=createDictionary('movies.txt',0,1,int,str,False)
  movieactor=createDictionary('movieactors.txt',0,1,int,int,True)
  actor=createDictionary('actors.txt',0,1,int,str,False)
  actorname=createDictionary('actors.txt',1,0,str,int,False)
  g=buildGraph(actor,movieactor)
  s=input('Enter the actor/actress you want to start from: ').rstrip()
  
  if s not in actorname:
    print('This person is not in the database')
  else:
    start=actorname[s]
    bfs(g,start)    
    name=input('Please enter an actor/actress name: ').rstrip()
    
    if name in actorname:
      n=actorname[name]
      print(getMessage(g,actor,movie,n,s))
      if g.getVertex(n).getDistance()==sys.maxsize: 
        print('The distance from '+name+' to Kevin Bacon is 0')
      else:
        print('The distance from '+name+' to Kevin Bacon is '+ \
            str(g.getVertex(n).getDistance()))
    else:
      print('This actor/actress is not in database')

if __name__=='__main__':
  main()
  
    
    
  