# You're given strings jewels representing the types of stones that are jewels, and stones representing the stones you have. 
# Each character in stones is a type of stone you have. You want to know how many of the stones you have are also jewels.

# Input: jewels = "aA", stones = "aAAbbbb"
# Output: 3

# T(n): O(m * n); S(n): O(1)
def numJewelsInStones(jewels, stones):
   count = 0
   for i in range(len(stones)):
       for j in range(len(jewels)):
           if stones[i] == jewels[j]:
               count += 1
               break
   return count

# T(n): O(m); S(n): O(1) as we have only characters to store
def numJewelsInStones(jewels, stones):
   j = set(jewels)
   count = 0
   for i in stones:
      if i in j:
            count += 1
   return count
