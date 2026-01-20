# Find an element in an array using linear search
# i/p: 1,2,3,4,5; target = 2, o/p: 1

# T(n): O(n), S(n): O(1)
def find_element(arr, target):
   for i in range(len(arr)):
      if arr[i] == target:
         return i 
   return -1

print(find_element([1,2,3,4,5], 10))

