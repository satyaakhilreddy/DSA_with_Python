import heapq;
import sys;

class Edge:

  def __init__(self,weight,start,end):
    self.weight=weight
    self.start=start
    self.end=end

class Node:

  def __init__(self,name):
    self.name=name
    self.visited=False
    self.neighbors=[]
    self.predecessor=None
    self.minDistance=sys.maxsize

  def __cmp__(self,other):
    return self.cmp(self.minDistance,other.minDistance)
  
  def __lt__(self,other):
    return self.minDistance<other.minDistance
  
class Dijkstra:

  def shortestPath(self,start):

    start.minDistance=0
    c=[]
    heapq.heappush(c,start)

    while len(c)>0:

      vertex=heapq.heappop(c)

      for v in vertex.neighbors:
        a=v.start
        b=v.end
        w=v.weight
        temp=a.minDistance+w

        if temp<b.minDistance:
          b.predecessor=a
          b.minDistance=temp
          heapq.heappush(c,b)
  
  def getPath(self,end):

    c=[]
    c.append(end.name)
    print("Distance : ",end.minDistance)
    node=end.predecessor:

    while node is not None:
      c.append(node.name)
      node=node.predecessor 
    
    return print("Shortest path : ",c)

        
        

