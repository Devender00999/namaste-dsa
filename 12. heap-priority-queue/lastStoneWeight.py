from typing import List
import heapq

def lastStoneWeight(self, stones: List[int]) -> int:
   pq = heapq.heapify_max(stones)
   
   while len(stones) > 1:
      y = heapq.heappop_max(stones)
      x = heapq.heappop_max(stones)

      if (y - x > 0):
            heapq.heappush_max(stones, y - x)
   return heapq.heappop_max(stones) if len(stones) > 0 else 0