# insertion sort
# i/p: [7, 4, 3, 5, 1, 2], o/p: [1, 2, 3, 4, 5, 7]

# T(n): O(n); S(n): O(1)
def insertion_sort(arr):
   for i in range(1, len(arr)):
      curr = arr[i]
      prev = i - 1
      while curr < arr[prev] and prev >= 0:
         arr[prev + 1] = arr[prev]
         prev -= 1
      arr[prev + 1] = curr
   return arr
      
print(insertion_sort([7, 4, 3, 5, 1, 2]))