class Stack:

  def __init__(self):
    self.stack=[]

  def isEmpty(self):
    if len(self.stack)==0:
      return True
    else:
      return False
  
  def push(self,data):
    self.stack.append(data)
  
  def pop(self):
    temp=self.stack[len(self.stack)-1]
    del self.stack[len(self.stack)-1]
    return temp
  
  def peek(self):
    return self.stack[len(self.stack)-1]

  def lenStack(self):
    return len(self.stack)
  
  def printStack(self):
    return print("Stack is : ",self.stack)

new=Stack()
new.push(1)
new.push(2)
new.push(3)
new.push(4)
new.push(5)

new.printStack()

d=new.pop()
print("Popped element is : ",d)
new.printStack()
print("Length of stack is : ",new.lenStack())
new.push(70)
new.printStack()
print("Elememt on top : ",new.peek())