# Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of
# days you have to wait after the ith day to get a warmer temperature. 
# If there is no future day for which this is possible, keep answer[i] == 0 instead.

# Input: temperatures = [73,74,75,71,69,72,76,73]
# Output: [1,1,4,2,1,1,0,0]


from typing import List


# T(n): O(n); S(n): O(n)
def dailyTemperatures(self, temp: List[int]) -> List[int]:
   res = [0] * len(temp)
   st1 = [len(temp) - 1]

   for i in range(len(temp) - 2, -1, -1):
      top = st1[len(st1) - 1]
      if temp[i] < temp[top]:
            res[i] = 1
      else:
            count = 0
            while len(st1) > 0:
               top = st1[len(st1) - 1]
               if (temp[i] < temp[top]):
                  res[i] = top - i
                  break
               else:
                  st1.pop()
            if len(st1) == 0:
               res[i] = 0
      st1.append(i)
   return res      

# T(n): O(n * m); S(n): O(n)
def dailyTemperatures(self, temp: List[int]) -> List[int]:
   map = {
      temp[len(temp) - 1]: 0
   }
   res = [0] * len(temp)
   st1 = [temp[len(temp) - 1]]
   st2 = []


   for i in range(len(temp) - 2, -1, -1):
      top = st1[len(st1) - 1]
      if temp[i] < top:
            res[i] = 1
      else:
            count = 0
            while len(st1) > 0:
               top = st1[len(st1) - 1]
               if (temp[i] < top):
                  count += 1
                  break
               else:
                  st2.append(st1.pop())
                  count += 1
            if len(st1) == 0:
               count = 0
            
            res[i] = count
            while len(st2) > 0:
               st1.append(st2.pop())

      st1.append(temp[i])
   return res  