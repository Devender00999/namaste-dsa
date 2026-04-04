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
      
   def heapifyUp(self, i):
      while i > 0:
         parentIdx = self.getParentIndex(i)
         if self.heap[i] < self.heap[parentIdx]:
            self.heap[i],self.heap[parentIdx] = self.heap[parentIdx], self.heap[i]
            i = parentIdx
         else:
            break
         
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
      
   def heapifyUp(self, i):
      while i > 0:
         parentIdx = self.getParentIndex(i)
         if self.heap[i] > self.heap[parentIdx]:
            self.heap[i],self.heap[parentIdx] = self.heap[parentIdx], self.heap[i]
            i = parentIdx
         else:
            break

heap = MaxHeap()

heap.insert(5)
heap.insert(10)
heap.insert(20)
heap.insert(30)
heap.insert(1)
heap.insert(31)
print(heap.heap)