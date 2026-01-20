# Selection sort
# i/p: [5, 2, 4, 1], o/[1, 2, 4, 5]

# T(n): O(n ^ 2); S(n): O(1)
def selection_sort(arr):
   for i in range(0, len(arr) - 1):
      min = i
      for j in range(i + 1, len(arr)):
         if arr[min] < arr[j]:
            min = j
            
      if min != i:
         arr[i], arr[min] = arr[min], arr[j]
      
      
arr = [5, 4, 2, 1, 10]
print(arr)
selection_sort(arr)
print(arr)