from queue import PriorityQueue
from typing import List


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minHeap = PriorityQueue()
        self.k = k
        for i in range(len(nums)):
            self.add(nums[i])

    def add(self, val: int) -> int:
        self.minHeap.put(val)
        if self.minHeap.qsize() > self.k:
            self.minHeap.get()
        return self.minHeap.queue[0]
     
     
