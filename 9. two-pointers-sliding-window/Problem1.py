from typing import List

# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]

# T(n): O(n^2); S(n): O(1)
def twoSum(self, arr: List[int], target: int) -> List[int]:
   for i in range(len(arr)):
      for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == target:
               return [i, j]


# T(n): O(n); S(n): O(n)
def twoSum(self, arr: List[int], target: int) -> List[int]:
   map = {}
   for i in range(len(arr)):
      map[arr[i]] = i
   print(map)
   for i in range(len(arr)):
      pairToFind = target - arr[i]
      if map.get(pairToFind) and map.get(pairToFind) != i:
            return [i, map[pairToFind]]