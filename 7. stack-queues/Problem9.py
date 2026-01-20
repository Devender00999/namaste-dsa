# Given a circular integer array nums (i.e., the next element of nums[nums.length - 1] is nums[0]), return the next greater number for every element in nums.
# The next greater number of a number x is the first greater number to its traversing-order next in the array,
# which means you could search circularly to find its next greater number. If it doesn't exist, return -1 for this number.

# Input: nums = [1,2,3,4,3]
# Output: [2,3,4,-1,4]

from typing import List

# T(n): O(n); S(n): O(n)
def nextGreaterElements(self, nums: List[int]) -> List[int]:
   arr = [*nums]
   result = [-1] * len(arr)
   stack = [arr[len(arr) - 1]]
   for i in range(len(arr) - 2, -1, -1):
      top = stack[len(stack) - 1]
      if arr[i] < top:
            result[i] = top
      else:
            while len(stack) > 0:
               top = stack[len(stack) - 1]
               if arr[i] < top:
                  result[i] = top
                  break
               else:
                  stack.pop()
            if len(stack) == 0:
               result[i] = -1
      stack.append(arr[i])
   for i in range(len(arr) - 1, -1, -1):
      top = stack[len(stack) - 1]
      if arr[i] < top:
            result[i] = top
      else:
            while len(stack) > 0:
               top = stack[len(stack) - 1]
               if arr[i] < top:
                  result[i] = top
                  break
               else:
                  stack.pop()
            if len(stack) == 0:
               result[i] = -1
      stack.append(arr[i])
   return result

# T(n): O(n); S(n): O(n)
def nextGreaterElements(self, nums: List[int]) -> List[int]:
   arr = [*nums]
   n = len(arr)
   result = [-1] * len(arr)
   stack = [arr[len(arr) - 1]]
   for i in range(2 * len(arr) - 2, -1, -1):
      top = stack[len(stack) - 1]
      if arr[i % n] < top:
            result[i % n] = top
      else:
            while len(stack) > 0:
               top = stack[len(stack) - 1]
               if arr[i % n] < top:
                  result[i % n] = top
                  break
               else:
                  stack.pop()
            if len(stack) == 0:
               result[i % n] = -1
      stack.append(arr[i % n])
   return result

# T(n): O(n)
def nextGreaterElements(self, nums: List[int]) -> List[int]:
   arr = [*nums, *nums]
   result = [-1] * len(arr)
   stack = [arr[len(arr) - 1]]
   for i in range(len(arr) - 2, -1, -1):
      top = stack[len(stack) - 1]
      if arr[i] < top:
            result[i] = top
      else:
            while len(stack) > 0:
               top = stack[len(stack) - 1]
               if arr[i] < top:
                  result[i] = top
                  break
               else:
                  stack.pop()
            if len(stack) == 0:
               result[i] = -1
      stack.append(arr[i])
   return result[:len(nums)]