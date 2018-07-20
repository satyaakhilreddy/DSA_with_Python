import heapq

class Vertex:
    
    def __init__(self,name):
        self.name=name
        self.neighbors=[]
    
    def __str__(self):
        return self.name

class Edge:
    def __init__(self,start,end,weight):
        self.weight=weight
        self.start=start
        self.end=end
    
    def __cmp__(self,other):
        return self.cmp(self.weight,other.weight)
    
    def __lt__(self,other):
        selfPriority = self.weight;
        otherPriority = other.weight;
        return selfPriority < otherPriority

class Prims:
    
    def __init__(self,vertices):
        self.vertices=vertices
        self.heap=[]
        self.c=[]
    
    def spanningtree(self,vertex):
        
        self.vertices.remove(vertex)
        
        while self.vertices:
            for e in vertex.neighbors:
                if e.end in self.vertices:
                    heapq.heappush(self.heap,e)
            
            mini=heapq.heappop(self.heap)
            self.c.append(mini)
            
            print(mini.start," - ",mini.end)
            
            vertex=mini.end
            self.vertices.remove(vertex)

node1 = Vertex("A");
node2 = Vertex("B");
node3 = Vertex("C");

edge1 = Edge(100,node1,node2);
edge2 = Edge(100,node2,node1);
edge3 = Edge(1000,node1,node3);
edge4 = Edge(1000,node3,node1);
edge5 = Edge(0.01,node3,node2);
edge6 = Edge(0.01,node2,node3);

node1.neighbors.append(edge1);
node1.neighbors.append(edge3);
node2.neighbors.append(edge2);
node2.neighbors.append(edge6);
node3.neighbors.append(edge4);
node3.neighbors.append(edge5);

unvisitedList = [];
unvisitedList.append(node1);
unvisitedList.append(node2);
unvisitedList.append(node3);

pri=Prims(unvisitedList)
pri.spanningtree(node2)

            
                
        