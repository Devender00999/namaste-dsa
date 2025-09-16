# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. 
# The relative order of the elements should be kept the same. Then return the number of unique elements in nums.
# i/p: [0,0,1,1,1,2,2,3,3,4]
# o/p: [0,1,2,3,4,_,_,_,_,_]

def remove_duplicate_sorted(nums: list):
   x = 0
   for i in range(len(nums)):
      if nums[i] > nums[x]:
         x += 1
         nums[x] = nums[i]
   return x + 1


