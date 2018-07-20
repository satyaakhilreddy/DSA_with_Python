class Node:

	def __init__(self,data):
		self.data=data
		self.left=None
		self.right=None
	
class BST:
	
	def __init__(self):
		self.root=None

	def insert(self,key):
		new=Node(key)
		
		if self.root==None:
			self.root=new
			return
		
		current=self.root
		p=1
		while(p):
			if key<current.data:
				if current.left!=None:
					current=current.left
				else:
					current.left=new
					p=0
			elif key>current.data:
				if current.right!=None:
					current=current.right
				else:
					current.right=new
					p=0
			else:
				print("Duplicate data")
				p=0
		
		return
	
	def remove(self,data):
		
		if self.root!=None:
			self.root=self.removeNode(self.root,data)
	
	def removeNode(self,node,data):
		
		if node==None:
			return node
		
		if data<node.data:
			node.left=self.removeNode(node.left,data)
		elif data>node.data:
			node.right=self.removeNode(node.right,data)
		else:
			if node.left==None and node.right==None:
				print("Leaf node")
				del node
				return None
			
			if node.left==None:
				print("Node with Right child")
				temp=node.right
				del node
				return temp
			elif node.right==None:
				print("Node with Left Child")
				temp=node.left
				del node
				return temp
			else:
				print("Node with two children")
				temp=self.getPrevious(node.left)
				node.data=temp.data
				node.left=self.removeNode(node.left,temp.data)
				
		return node
	
	def getPrevious(self,node):
		
		if node.right!=None:
			return self.getPrevious(node.right)
		
		return node
	
	def getMin(self):
		
		if self.root==None:
			print("No nodes in the tree")
			return
		
		current=self.root
		
		while(current.left!=None):
				current=current.left
				min=current.data
		
		return min
	
	def getMaxValue(self):
		
		if self.root!=None:
			return self.getMax(self.root.right)
	
	def getMax(self,node):
		
		if node.right!=None:
			return self.getMax(node.right)
		
		return node.data

	def inorder(self):
		c=[]
		if self.root!=None:
			self.traverse(self.root,c)
			return c
	
	def traverse(self,node,c):
		
		if node.left!=None:
			self.traverse(node.left,c)
		
		c.append(node.data)
		
		if node.right!=None:
			self.traverse(node.right,c)
	
tree=BST()
tree.insert(10)
tree.insert(5)
tree.insert(15)
tree.insert(6)

print(tree.getMaxValue())
print(tree.getMin())
print(tree.inorder())

tree.remove(6)
print(tree.inorder())

		
		