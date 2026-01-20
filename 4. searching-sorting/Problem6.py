# Merge sort

# T(n): O(n^2), S(n): O(n)
def merge(arr1, arr2):
   i = 0
   j = 0
   m = len(arr1)
   n = len(arr2)
   arr = []
   while i < m and j < n:
      if arr1[i] < arr2[j]:
         arr.append(arr1[i])
         i += 1
      else:
         arr.append(arr2[j])
         j += 1
   while (i < m):
      arr.append(arr1[i])
      i += 1
   while (j < n):
      arr.append(arr2[j])
      j += 1
   return arr
   

# T(n): O(n^2), S(n): O(n)
def merge_sort(nums):
   if len(nums) == 1:
      return nums

   mid = len(nums) //2
   left = merge_sort(nums[:mid])
   right = merge_sort(nums[mid:])

   return merge(left, right)

print(merge_sort([8,4,5,6,9,1,3,6]))