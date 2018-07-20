class Queue:

  def __init__(self):
    self.queue=[]
  
  def isEmpty(self):
    if len(self.queue)==0:
      return True
    else:
      return False
  
  def enqueue(self,data):
    self.queue.append(data)
  
  def dequeue(self):
    temp=self.queue[0]
    del self.queue[0]
    return temp
  
  def peek(self):
    return self.queue[0]
  
  def lenQueue(self):
    return len(self.queue)
  
  def traverse(self):
    return print("The queue is : ",self.queue)
  
q=Queue()

print(q.isEmpty())

q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)

q.traverse()

print("Dequeued element : ",q.dequeue())

print("First element : ",q.peek())

print("Length of the queue : ",q.lenQueue())


  
