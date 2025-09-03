# write a function to find an element inside an array and return it's index.
# if the element is not present return -1
def search_an_element(arr, elem):
   for i in range(0, len(arr)):
      if arr[i] == elem:
         return i
   return -1

# print(search_an_element([1,2,4,5,6], 2))
# print(search_an_element([1,2,4,5,6], 3))

# write a function that return numbers of negative numbers in array
def negative_number_count(arr):
   negative_count = 0
   for i in range(0, len(arr)):
      if arr[i] < 0:
         negative_count += 1
   return negative_count

# print(negative_number_count([10, -1, 2, -30]))

# write a function that return largest number in array
def largest_number(arr):
   largest = arr[0]
   for i in range(0, len(arr)):
      if arr[i] > largest:
         largest = arr[i]
   return largest

# print(largest_number([10, -1, 2, 30]))

# write a function that return largest number in array
def smallest_number(arr):
   smallest = arr[0]
   for i in range(0, len(arr)):
      if arr[i] < smallest:
         smallest = arr[i]
   return smallest

# print(smallest_number([10, -100, 2, 30]))


# write a function to find the second largest number in array
def second_largest(arr):
   largest = largest_number(arr)
   second_largest = arr[0]
   for i in range(0, len(arr)):
      if arr[i] > second_largest and arr[i] < largest:
         second_largest = arr[i]
   return second_largest

# write a function to find the second largest number in array
def second_largest_v2(arr):
   largest = -float('inf')
   second_largest = -float('inf')
   for i in range(0, len(arr)):
      if arr[i] > largest:
         second_largest = largest
         largest = arr[i]
      elif arr[i] > second_largest and arr[i] != largest:
         second_largest = arr[i]
   return second_largest

print(second_largest_v2([10, 102, 233, 20, 12, 230]))
# print(second_largest([10, 102, 230, 20, 12, 230]))
