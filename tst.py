
class Node:

  def __init__(self,letter):
    self.letter=letter
    self.left=None
    self.right=None
    self.middle=None
    self.value=0

class TST:

  def __init__(self):
    self.root=None

  def put(self,key,value):
    self.root=self.putnode(self.root,key,value,0)
  
  def putnode(self,node,key,value,index):
    
    if node==None:
      node=Node(key[index])
    
    if key[index]<node.letter:
      node.left=self.putnode(node.left,key,value,index)
    elif key[index]>node.letter:
      node.right=self.putnode(node.right,key,value,index)
    elif index<(len(key)-1):
      node.middle=self.putnode(node.middle,key,value,index+1)
    else:
      node.value=value
    
    return node
  
  def get(self,key):

    node=self.getnode(self.root,key,0)

    if node is None:
      return print("No such key")
    
    return node.value
  
  def getnode(self,node,key,index):

    if node is None:
      return None
    
    if key[index]<node.letter:
      return self.getnode(node.left,key,index)
    elif key[index]>node.letter:
      return self.getnode(node.right,key,index)
    elif index<(len(key)-1):
      return self.getnode(node.middle,key,index+1)
    else:
      return node
  
tst=TST()

tst.put('one',1)
tst.put('two',2)

print(tst.get('two'))
  

      
    
