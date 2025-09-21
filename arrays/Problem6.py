# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
# Note that you must do this in-place without making a copy of the array.
# i/p: [0,1,0,3,12]
# o/p: [1,3,12,0,0]


def move_zeros(nums):
   n = len(nums)
   temp = [0] * n
   x = 0
   for i in range(n):
      if nums[i] != 0:
         temp[x] = nums[i]   
         x += 1
   return temp


def move_zeros(nums):
   n = len(nums)
   x = 0
   for i in range(0, n):
      if nums[i] != 0:
         nums[x] = nums[i]
         x += 1
   for i in range(x, n):
      nums[i] = 0
   return nums
         

print(move_zeros([0,1,0,3,12]))