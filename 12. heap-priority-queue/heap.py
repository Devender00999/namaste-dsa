import math
class MinHeap:
   def __init__(self):
      self.heap = []
      
   def getLeftChildIndex(self, i): 
      return (2 * i) + 1
   
   def getRightChildIndex(self, i):
      return 2 * i + 2
   
   def getParentIndex(self, i):
      return (i - 1) // 2
   
   def insert(self, elem):
      self.heap.append(elem)
      self.heapifyUp(len(self.heap) - 1)
      
   def extract(self):
      if (len(self.heap) == 0): return
      self.heap[0] = self.heap[len(self.heap) - 1]
      self.heap.pop()
      self.heapifyDown(0)
      
   def heapifyUp(self, i):
      while i > 0:
         parentIdx = self.getParentIndex(i)
         if self.heap[i] < self.heap[parentIdx]:
            self.heap[i],self.heap[parentIdx] = self.heap[parentIdx], self.heap[i]
            i = parentIdx
         else:
            break
         
   def heapifyDown(self, i = 0):
      left = self.getLeftChildIndex(i)
      right = self.getRightChildIndex(i);
      n = len(self.heap)
      smallest = i
      if (left < n and self.heap[left] < self.heap[smallest]):
         smallest = left
      if (right < n and self.heap[right] < self.heap[smallest]):
         smallest = right
      
      if (smallest != i):
         self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
         self.heapifyDown(smallest)
      
               
class MaxHeap:
   def __init__(self):
      self.heap = []
      
   def getLeftChildIndex(self, i): 
      return (2 * i) + 1
   
   def getRightChildIndex(self, i):
      return 2 * i + 2
   
   def getParentIndex(self, i):
      return (i - 1) // 2
   
   def insert(self, elem):
      self.heap.append(elem)
      self.heapifyUp(len(self.heap) - 1)
      
   def extract(self):
      if (len(self.heap) == 0): return
      self.heap[0] = self.heap[len(self.heap) - 1]
      self.heap.pop()
      self.heapifyDown(0)
      
   def heapifyUp(self, i):
      while i > 0:
         parentIdx = self.getParentIndex(i)
         if self.heap[i] > self.heap[parentIdx]:
            self.heap[i],self.heap[parentIdx] = self.heap[parentIdx], self.heap[i]
            i = parentIdx
         else:
            break
   def heapifyDown(self, i = 0):
      left = self.getLeftChildIndex(i)
      right = self.getRightChildIndex(i);
      n = len(self.heap)
      greatest = i
      if (left < n and self.heap[left] > self.heap[greatest]):
         greatest = left
      if (right < n and self.heap[right] > self.heap[greatest]):
         greatest = right
      
      if (greatest != i):
         self.heap[i], self.heap[greatest] = self.heap[greatest], self.heap[i]
         self.heapifyDown(greatest)


heap = MaxHeap()

heap.insert(5)
heap.insert(30)
heap.insert(10)
heap.insert(20)

print(heap.heap)
heap.extract()
# heap.extract()
# heap.extract()
# heap.extract()
# heap.extract()
print(heap.heap)
