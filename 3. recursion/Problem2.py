# find the sum of all elements in an array

def sum_of_elem(arr):
   if len(arr) == 1:
      return arr[0]
   return arr[0] + sum_of_elem(arr[1:])


def sum_of_odd_elem(arr):
   if len(arr) == 0:
      return 0
   
   if arr[0] % 2 != 0:
      return arr[0] +  sum_of_odd_elem(arr[1:])
   return sum_of_odd_elem(arr[1:])
      
      
print(sum_of_odd_elem([5,4,3,2,1]))