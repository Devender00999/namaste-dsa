from typing import List

# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.
# If target is not found in the array, return [-1, -1].

# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]

def searchRange(self, nums: List[int], target: int) -> List[int]:
   l = 0; r = len(nums) - 1
   first = -1; last = -1
   while l <= r:
      m = l + (r - l) // 2
      if nums[m] == target:
            first = m
            r = m - 1
      elif nums[m] < target:
            l = m + 1
      else:
            r = m - 1

   if first != -1:
      l = first; r = len(nums) - 1
      while l <= r:
            m = l + (r - l) // 2
            if nums[m] == target:
               last = m
               l = m + 1
            elif nums[m] < target:
               l = m + 1
            else:
               r = m - 1

   return [first, last]
