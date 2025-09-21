# Given a binary array nums, return the maximum number of consecutive 1's in the array.
# i/p: [1,1,0,1,1,1], o/p: 3

# T(n): O(n), S(n): O(1)
def findMaxConsecutiveOnes(nums: list):
   max_count = 0
   curr = 0
   for i in range(len(nums)):
      if nums[i] == 0:
         max_count = max(max_count, curr)
         curr = 0
      else:
         curr += 1
   if max_count < curr:
      max_count = curr
   return max(max_count, curr)



print(findMaxConsecutiveOnes([1,1,0,1,1,1]))