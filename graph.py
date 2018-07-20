
class Vertex:

  def __init__(self,name):
    self.name=name
    self.neighbours=[]
    self.visited=False
  
class Graph:

  def bfs(self,vertex):

    q=[]
    c=[]
    q.append(vertex)
    vertex.visited=True

    while len(q) is not 0:
      temp=q.pop(0)
      c.append(temp.name)

      for i in temp.neighbours:
        if i.visited is False:
          q.append(i)
          i.visited=True
    
    return print("The BFS is : ",c)
  
  def dfs(self,vertex):

    c=[]
    self.dfsearch(vertex,c)
    return print("The DFS is : ",c)
  
  def dfsearch(self,vertex,c):

    c.append(vertex.name)
    vertex.visited=True

    for v in vertex.neighbours:
      if v.visited is False:
        self.dfsearch(v,c)


ver1=Vertex("A")
ver2=Vertex("B")
ver3=Vertex("C")
ver4=Vertex("D")
ver5=Vertex("E")

ver1.neighbours.append(ver2)
ver1.neighbours.append(ver4)
ver2.neighbours.append(ver3)
ver3.neighbours.append(ver5)

g=Graph()

g.dfs(ver1)

