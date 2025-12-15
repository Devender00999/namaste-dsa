from typing import List

# Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number.
# Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]

# T(n): O(n); S(n): O(1)
def twoSum(self, arr: List[int], target: int) -> List[int]:
   l = 0; r = len(arr) - 1
   while l < r:
      sum = arr[l] + arr[r]
      if sum == target:
            return [l + 1, r + 1]
      elif sum < target:
            l = l + 1
      else:
            r = r - 1