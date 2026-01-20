# Suppose an array of length n sorted in ascending order is rotated between 1 and n times. 
# For example, the array nums = [0,1,2,4,5,6,7] might become:

# Input: nums = [3,4,5,1,2]
# Output: 1
# Explanation: The original array was [1,2,3,4,5] rotated 3 times.


from typing import List
# T(n): O(logn)
def findMin(self, arr: List[int]) -> int:
   l = 0; r = len(arr) - 1
   while l <= r:
      if (arr[l] <= arr[r]):
            return arr[l]

      m = l + (r - l) // 2
      print(l, r, m)

      if arr[m] < arr[m-1]:
            return arr[m]

      if arr[l] > arr[m]:
            r = m - 1
      else:
            l = m + 1
   return -1


# T(n): O(logn)
def findMin(self, nums: List[int]) -> int:
   l = 0; r = len(nums) - 1
   min = nums[0]
   while l <= r:
      m = l + (r - l) // 2
      if nums[l] <= nums[m]:
            if nums[l] < min:
               min = nums[l]
            l = m + 1
      else:
            if nums[m] < min:
               min = nums[m]
            r = m
   return min