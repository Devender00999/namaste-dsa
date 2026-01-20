# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

# T(n): O(1) for all, S(n): O(n)
class MinStack:
   def __init__(self):
      self.st1 = []
      self.st2 = []
      

   def push(self, val: int) -> None:
      self.st1.append(val)
      if (len(self.st2) == 0):
         self.st2.append(val)
      else:
         top = self.st2[len(self.st2) - 1]
         if top >= val:
               self.st2.append(val)
      

   def pop(self) -> None:
      top = self.st1.pop()
      if len(self.st2) > 0 and top == self.st2[len(self.st2) - 1]:
         self.st2.pop()

   def top(self) -> int:
      return self.st1[len(self.st1) - 1]

   def getMin(self) -> int:
      if len(self.st2) > 0:
         return self.st2[len(self.st2) - 1]
      

# T(n): O(1) for all, S(n): O(1)
class MinStack:
   def __init__(self):
        self.st1 = []
        
   def push(self, val: int) -> None:
      if len(self.st1) == 0:
         self.st1.append({ "value": val, "min": val})
      else:
         top = len(self.st1) - 1
         if self.st1[top]["min"] <= val:
               self.st1.append({ "value": val, "min": self.st1[top]['min']})
         else:
               self.st1.append({ "value": val, "min": val})

   def pop(self) -> None:
      self.st1.pop()

   def top(self) -> int:
      return self.st1[len(self.st1) - 1]['value']

   def getMin(self) -> int:
      if len(self.st1) > 0:
         return self.st1[len(self.st1) - 1]['min']

      