from typing import List

# You are given an integer mountain array arr of length n where the values increase to a peak element and then decrease.

# Input: arr = [0,1,0]
# Output: 1

def peakIndexInMountainArray(self, arr: List[int]) -> int:
   l = 0; r = len(arr) - 1
   max = -1
   while l < r:
      m = l + (r - l) // 2
      if arr[m - 1] < arr[m] and arr[m + 1] < arr[m]:
            return m
      elif arr[m] < arr[m + 1]:
            l = m
      else:
            r = m
   return max