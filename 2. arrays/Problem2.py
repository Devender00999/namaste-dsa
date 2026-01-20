# Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. 
# The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

def removeElement(arr, n):
   x = 0
   for i in range(len(arr)):
      if arr[i] != n:
         arr[x] = arr[i]
         x += 1
   return x 
   
print(removeElement([0,1,2,2,3,0,4,2], 2))
