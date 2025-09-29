# Bubble sort
# i/p: [5, 2, 4, 1], o/[1, 2, 4, 5]

# T(n): O(n ^ 2); S(n): O(1)
def bubble_sort(arr):
   for i in range(len(arr) - 1):
      is_swapped = False
      for j in range(len(arr) - i - 1):
         if (arr[j] > arr[j + 1]):
            
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            is_swapped = True
            
      if not is_swapped:
         break
   
   return arr

arr = [5, 4, 2, 1, 10]
# arr = [1, 2, 3, 4, 5]
print(arr)
bubble_sort(arr)
print(arr)