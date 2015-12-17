import sys

class Vertex:
    def __init__(self,key):
        self.id = key
        self.connectedTo = {}
        self.color = 'white'
        self.dist = sys.maxsize
        self.pred = None
        self.disc = 0
        self.fin = 0
        #self.cost = {}

    def addNeighbor(self,nbr,weight=0):
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id) + ' connectedTo: '+ str([x.id for x in self.connectedTo])

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self,nbr):
        return self.connectedTo[nbr]

    #def getCost(self,nbr):
     #   return self.cost[nbr]
    #def setCost(self,nbr,cost):
     #   self.cost[nbr] = cost
    def setColor(self,color):
        self.color = color
    def setDistance(self,d):
        self.dist = d
    def setPred(self,p):
        self.pred = p
    def setDiscovery(self,dtime):
        self.disc = dtime
    def setFinish(self,ftime):
        self.fin = ftime
    def getFinish(self):
        return self.fin
    def getDiscovery(self):
        return self.disc
    def getPred(self):
        return self.pred
    def getDistance(self):
        return self.dist
    def getColor(self):
        return self.color
#    def getAdj(self):
#        return self.adj
#    def getId(self):
#        return self.id