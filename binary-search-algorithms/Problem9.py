def singleNonDuplicate(self, nums: List[int]) -> int:
   arr = {}
   for i in nums:
      if arr.get(i) is None:
            arr[i] = 1
      else:
            arr[i] += 1
   
   for i in arr.keys():
      if arr[i] == 1:
            return i 

def singleNonDuplicate(self, arr: List[int]) -> int:
   l = 0; r = len(arr) - 1
   while l <= r:
      m = l + (r - l) // 2
      # pair in left
      if l == m and m == r:
            return arr[m]
      if arr[m] == arr[m - 1]:
            leftOdd = m - 1 - l
            if leftOdd % 2 == 1:
               r = m - 2
            else:
               l = m + 1

      # pair in right
      elif arr[m] == arr[m + 1]:
            leftOdd = m - l
            if leftOdd % 2 == 1:
               r = m - 1
            else:
               l = m + 2
      else:
            return arr[m]