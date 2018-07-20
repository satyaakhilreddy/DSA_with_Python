class Vertex:
    
    def __init__(self,name):
        self.name=name
        self.node=None

class Node:
    
    def __init__(self,height,nodeID,parent):
        self.height=height
        self.nodeID=nodeID
        self.parent=parent
    
class Edge:
    
    def __init__(self,weight,start,end):
        self.weight=weight
        self.start=start
        self.end=end
    
    def __cmp__(self,other):
        return self.cmp(self.weight,other.weight)
    
    def __lt__(self,other):
        return self.weight<other.weight

class disjoint:
    
    def __init__(self,vertices):
        self.vertices=vertices
        self.nodeCount=0
        self.rootNodes=[]
        self.setCount=0
        self.makeSets(vertices)
    
    def find(self,node):
        
        current=node
        
        # Finding the root node
        while current.parent is not None:
            current=current.parent
        
        root=current
        current=node
        
        " PATH COMPRESSION "
        while current is not root:
            temp=current.parent
            current.parent=root
            current=temp
        
        return root.nodeID
    
    def merge(self,a,b):
        
        ind1=self.find(a)
        ind2=self.find(b)
        
        if ind1==ind2:
            return
        
        root1=self.rootNodes[ind1]
        root2=self.rootNodes[ind2]
        
        if root1.height<root2.height:
            root1.parent=root2
        elif root2.height<root1.height:
            root2.parent=root1
        else:
            root2.parent=root1.parent
            root1.height=root1.height+1
    
    def makeSets(self,vertices):
        for i in vertices:
            self.makeset(i)
    
    def makeset(self,v):
        node=Node(0,len(self.rootNodes),None)
        v.node=node
        self.rootNodes.append(v)
        self.setCount=self.setCount+1
        self.nodeCount=self.nodeCount+1

class Kruskal:
    
    def spanningTree(self,vertices,edges):
        
        disj=disjoint(vertices)
        tree=[]
        edges.sort()
        
        for e in edges:
            u=e.start.node
            v=e.end.node
            
            if disj.find(u) is not disj.find(v):
                disj.merge(u,v)
                tree.append(e)
        
        for t in tree:
            print(t.start," - ",t.end)
    

vertex1 = Vertex("a");
vertex2 = Vertex("b");
vertex3 = Vertex("c");
vertex4 = Vertex("d");
vertex5 = Vertex("e");
vertex6 = Vertex("f");
vertex7 = Vertex("g");

edge1 = Edge(2,vertex1,vertex2);
edge2 = Edge(6,vertex1,vertex3);
edge3 = Edge(5,vertex1,vertex5);
edge4 = Edge(10,vertex1,vertex6);
edge5 = Edge(3,vertex2,vertex4);
edge6 = Edge(3,vertex2,vertex5);
edge7 = Edge(1,vertex3,vertex4);
edge8 = Edge(2,vertex3,vertex6);
edge9 = Edge(4,vertex4,vertex5);
edge10 = Edge(5,vertex4,vertex7);
edge11 = Edge(5,vertex6,vertex7);


vertexList = [];
vertexList.append(vertex1);
vertexList.append(vertex2);
vertexList.append(vertex3);
vertexList.append(vertex4);
vertexList.append(vertex5);
vertexList.append(vertex6);
vertexList.append(vertex7);

edgeList = [];
edgeList.append(edge1);
edgeList.append(edge2);
edgeList.append(edge3);
edgeList.append(edge4);
edgeList.append(edge5);
edgeList.append(edge6);
edgeList.append(edge7);
edgeList.append(edge8);
edgeList.append(edge9);
edgeList.append(edge10);
edgeList.append(edge11);

k=Kruskal()
k.spanningTree(vertexList,edgeList)


                
         
    
    