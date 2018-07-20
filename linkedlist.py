class Node:
    
    def __init__(self,data):
        self.next=None
        self.data=data
        
class LinkedList:
    
    def __init__(self):
        self.head=None
    
    def insertStart(self,key):
        new=Node(key)
        
        if self.head==None:
            self.head=new
        else:
            new.next=self.head
            self.head=new
    
    def insertEnd(self,key):
        new=Node(key)
        
        current=self.head
        p=1
        
        while(p):
            if current.next==None:
                current.next=new
                p=0
            else:
              current=current.next
    
    def remove(self,key):
        
        if self.head is None:
            return
        
        current=self.head
        parent=None
        p=1
        
        while(p):
            if current.data!=key:
                parent=current
                current=current.next
            else:
                if parent is None:
                    self.head=current.next
                    p=0
                else:
                    parent.next=current.next
                    p=0
    
    def traverse(self):
        
        current=self.head
        l=[]
        p=1
        
        while(p):
            if current!=None:
                l.append(current.data)
                current=current.next
            else:
                p=0
        
        return print("The linked list is : ",l)

ll=LinkedList()

ll.insertStart(1)
ll.insertStart(2)
ll.insertEnd(3)
ll.remove(3)

ll.traverse()
