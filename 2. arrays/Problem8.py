# Given an array nums containing n distinct numbers in the range [0, n], 
# return the only number in the range that is missing from the array.

# i/p: [9,6,4,2,3,5,7,0,1]
# o/p: 8

# T(n): O(n), S(n): O(1)
def not_in_array(nums):
   n = len(nums)
   arr = []
   for i in range(len(nums)):
      arr.append(nums[i])
   for i in range(n):
      idx = nums[i]
      if idx < n:
         arr[idx] = -1
   for i in range(n):
      if arr[i] != -1:
         return i
   return n

# T(n): O(n), S(n): O(1)
def not_in_array(nums):
   n = len(nums)
   total_sum = (n * (n + 1)) // 2
   
   partial_sum = 0
   for i in range(n):
      partial_sum += nums[i]
   return total_sum - partial_sum

print(not_in_array([3, 2, 1]))
print(not_in_array([0, 1]))
print(not_in_array([9,6,4,2,3,5,7,0,1]))