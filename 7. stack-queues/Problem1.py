# Stack 

class MyStack:
   def __init__(self):
      self.queue = []
      self.helper = []
      self.topIdx = -1
      

   def push(self, x: int) -> None:
      self.queue.append(x)
      self.topIdx += 1

   def pop(self) -> int:
      l = len(self.queue)
      for i in range(l - 1):
         self.helper.append(self.queue.pop(0))
      item = self.queue.pop(0)
      self.queue = self.helper
      self.helper = []
      self.topIdx -= 1
      return item
               

   def top(self) -> int:
      # return self.queue[self.topIdx]
      l = len(self.queue)
      for i in range(l - 1):
         self.helper.append(self.queue.pop(0))
      last = self.queue.pop(0)
      self.helper.append(last)
      self.queue = self.helper
      self.helper = []
      return last
      

   def empty(self) -> bool:
      return self.topIdx == -1
   
class MyStack:
   def __init__(self):
      self.queue = []

   def push(self, x: int) -> None:
      self.queue.append(x)

   def pop(self) -> int:
      l = len(self.queue)
      for i in range(l - 1):
         self.queue.append(self.queue.pop(0))
      return self.queue.pop(0)

   def top(self) -> int:
      l = len(self.queue)
      for i in range(l - 1):
         self.queue.append(self.queue.pop(0))
      last = self.queue.pop(0)
      self.queue.append(last)        
      return last
      
   def empty(self) -> bool:
      return len(self.queue) == 0

   
stack = MyStack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.pop())
# print(stack.top())