# A peak element is an element that is strictly greater than its neighbors.

# Input: nums = [1,2,1,3,5,6,4]
# Output: 5

def findPeakElement(self, nums: List[int]) -> int:
   l = 0; r = len(nums) -1 
   while l < r:
      m = l + (r - l) // 2
      if nums[m + 1] > nums[m]:
            l = m + 1
      else:
            r = m
   return r