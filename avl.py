
class Node:
  
  def __init__(self,data):
    self.data=data
    self.height=0
    self.left=None
    self.right=None
  
class AVL:

  def __init__(self):
    self.root=None

  def insert(self,data):
    self.root=self.insertNode(data,self.root)
  
  def insertNode(self,data,node):
    if node==None:
      new=Node(data)
      return new
    
    if data<node.data:
      node.left=self.insertNode(data,node.left)
    if data>node.data:
      node.right=self.insertNode(data,node.right)
    
    node.height=max(self.calcHeight(node.right),self.calcHeight(node.left))+1

    return self.checkTree(data,node)
  
  def checkTree(self,data,node):
    bal=self.Balance(node)

    if bal>1 and data<node.left.data:
      print("Doubly left heavy situation")
      return self.rotateRight(node)  
    
    if bal<-1 and data>node.right.data:
      print("Doubly right heavy situation")
      return self.rotateLeft(node)
    
    if bal>1 and data>node.left.data:
      print("Left-right heavy")
      node.left=self.rotateLeft(node.left)
      return self.rotateRight(node)
    
    if bal<-1 and data<node.right.data:
      print("Right-left heavy")
      node.right=self.rotateRight(node.right)
      return self.rotateLeft(node)   
    
    return node
  
  def delete(self,data):
    if self.root is not None:
      self.root=self.deleteNode(data,self.root)
  
  def deleteNode(self,data,node):
    if node is None:
      return node
    
    if data<node.data:
      node.left=self.deleteNode(data,node.left)
    if data>node.data:
      node.right=self.deleteNode(data,node.right)
    else:
      if node.left==None and node.right==None:
        print("Node with no children..")
        del node
        return None
      
      if node.right==None and node.left!=None:
        print("Node with left child...")
        temp=node.left
        del node
        return temp
      
      if node.right!=None and node.left==None:
        print("Node with right child...")
        temp=node.right
        del node
        return temp
      
      print("Node has two children...")
      temp=self.getPredecessor(node.left)
      node.data=temp.data
      node.left=self.deleteNode(temp.data,node.left)
    
    if not node:
      return node
    
    node.height=max(self.calcHeight(node.left),self.calcHeight(node.right))+1

    bal=self.Balance(node)

    if bal>1 and self.Balance(node.left)>=0:
      return self.rotateRight(node)
    if bal>1 and self.Balance(node.left)<0:
      node.left=self.rotateLeft(node.left)
      return self.rotateRight(node)
    if bal<-1 and self.Balance(node.right)<=0:
      return self.rotateLeft(node)
    if bal<-1 and self.Balance(node.right)>0:
      node.right=self.rotateRight(node.right)
      return self.rotateLeft(node)
    
    return node
  
  def getPredecessor(self,node):
    if node is not None:
      return self.getPredecessor(node.right)
    return node
    

  def inorder(self):
    c=[]
    if self.root is not None:
      self.traverse(self.root,c)
      return print("The inorder traversal is : ",c)
	
  def traverse(self,node,c):
    if node.left!=None:
      self.traverse(node.left,c)

    c.append(node.data)
		
    if node.right!=None:
      self.traverse(node.right,c)

  def calcHeight(self,node):
    if node==None:
      return -1
    return node.height
  
  def Balance(self,node):
    if node==None:
      return 0
    return self.calcHeight(node.left)-self.calcHeight(node.right)
  
  def rotateRight(self,node):
    print("Right Rotation of node : ",node.data)
    temp=node.left
    t=temp.right
    temp.right=node
    node.left=t

    node.height=max(self.calcHeight(node.left),self.calcHeight(node.right))+1
    temp.height=max(self.calcHeight(temp.left),self.calcHeight(temp.right))+1

    return temp
  
  def rotateLeft(self,node):
    print("Left Rotation of node : ",node.data)
    temp=node.right
    t=temp.left
    temp.left=node
    node.right=t

    node.height=max(self.calcHeight(node.left),self.calcHeight(node.right))+1
    temp.height=max(self.calcHeight(temp.left),self.calcHeight(temp.right))+1

    return temp

avl=AVL()
avl.insert(10)
avl.insert(20)
avl.insert(5)
avl.insert(4)
avl.insert(15)

avl.inorder

avl.delete(20)


avl.inorder()