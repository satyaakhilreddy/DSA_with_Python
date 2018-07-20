# Heap Data Structure

class Heap:

  heap_size=10

  def __init__(self):
    
    self.heap=[]
    self.position=-1
  
  def insert(self,data):
    
    if self.isFull():
      print("Heap is full...")
      return
    
    self.heap.append(data)
    self.position+=1
    self.checkup(self.position)
  
  def isFull(self):
    
    if self.position==Heap.heap_size-1:
      return True
    else:
      return False

  def checkup(self,ind):

    parent=int((ind-1)/2)

    while parent>=0 and self.heap[parent]<self.heap[ind]:
      temp=self.heap[ind]
      self.heap[ind]=self.heap[parent]
      self.heap[parent]=temp
      ind=parent
      parent=int((ind-1)/2)
  
  def heapsort(self):
    c=[]
    for i in range(0,self.position+1):
      temp=self.heap[0]
      c.append(temp)
      self.heap[0]=self.heap[self.position-i]
      self.heap[self.position-i]=temp
      self.checkdown(0,self.position-i-1)
    
    return print(c)
  
  def checkdown(self,ind,last):

    while ind<last:
      left=2*ind+1
      right=2*ind+2
      if left<last:
        if right<last:
          if self.heap[left]>self.heap[ind]:
            temp=self.heap[ind]
            self.heap[ind]=self.heap[left]
            self.heap[left]=temp
            ind=left
          if self.heap[right]>self.heap[ind]:
            temp=self.heap[ind]
            self.heap[ind]=self.heap[right]
            self.heap[right]=temp
            ind=right
        if right>last:
          if self.heap[left]>self.heap[ind]:
            temp=self.heap[ind]
            self.heap[ind]=self.heap[left]
            self.heap[left]=temp
            ind=left
          else:
            break
      else:
        break

heap=Heap()
heap.insert(10)
heap.insert(40)
heap.insert(30)
heap.insert(20)
print(heap.heap)

heap.heapsort()


