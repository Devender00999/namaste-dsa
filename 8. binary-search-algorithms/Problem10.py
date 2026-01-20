from typing import List

# Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array. 
# The result should also be sorted in ascending order.

# Input: arr = [1,2,3,4,5], k = 4, x = 3
# Output: [1,2,3,4]

# T(n): O(n)
# S(n): O(1)
def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
   i = 0
   while i + k < len(arr) and  (x - arr[i] > arr[i + k] - x):
      i += 1
   print(i)
   return arr[i:i + k]

# T(n): O(logn)
# S(n): O(1)
def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
   l = 0; r = len(arr) - 1
   while l < r:
      m = l + (r - l) // 2
      if m + k < len(arr) and (arr[m + k] - x) < (x - arr[m]):
            l = m + 1
      else:
            r = m
   return arr[r: r+k]