from typing import List
from queue import PriorityQueue


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        queue = PriorityQueue()
        for i in range(len(nums)):
            queue.put(nums[i])
            if queue.qsize() > k:
                queue.get()

        return queue.get()


sol = Solution()
print(sol.findKthLargest([3, 2, 1, 5, 6, 4], 2))
