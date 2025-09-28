# Binary search
# i/p: 1,2,3,4,5; target = 2, o/p: 1

# T(n): O(logn), S(n): O(1)
def binary_search(nums, target):
   l = 0
   r = len(nums) - 1
   mid = (l + r) // 2
   
   while(l <= r):
      if nums[mid] == target:
         return mid
      elif nums[mid] < target:
         l = mid + 1
      else:
         r = mid - 1
      mid = (l + r) // 2
   return -1

print(binary_search([1], 1))
