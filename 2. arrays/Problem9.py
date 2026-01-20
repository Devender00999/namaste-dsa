# Given a non-empty array of integers nums, every element appears twice except for one. 
# Find that single one.

# i/p: [4,1,2,1,2], o/p: 4
# T(n): O(n), S(n): O(n)
def single_number(nums: list):
   li = {}
   for i in range(len(nums)):
      if li.get(nums[i], -1) != -1:
         li[nums[i]] = li[nums[i]] + 1
      else:
         li[nums[i]] = 1
   for i in li.keys():
      if li[i] == 1:
         return i
    
# T(n): O(n), S(n): O(1)  
def single_number(nums: list):
   res = nums[0]
   for i in range(1, len(nums)):
      res ^= nums[i]
   return res

print(single_number([4,1,2,1,2]))
print(single_number([4]))