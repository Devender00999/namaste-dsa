# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".

# Example
# Input: strs = ["flower","flow","flight"]
# Output: "fl"

def longestCommonPrefixV1(self, strs):
   """
   :type strs: List[str]
   :rtype: str
   """
   n = len(strs)
   x = 0
   smallest = len(strs[0])
   for i in range(1, n):
      if smallest > len(strs[i]):
            smallest = len(strs[i])
   
   for i in range(smallest):
      isSame = True
      prev = strs[0]
      for j in range(1, n):
            if prev[i] != strs[j][i]:
               isSame = False
               break
      
      if not isSame:
            break
      x += 1
   return str[0][0:x]

# T(n): O(sum of length of all strings); S(n): O(1)
def longestCommonPrefixV1(strs):
   x = 0
   n = len(strs)
   while x < len(strs[0]):
      prev = strs[0]
      for j in range(1, n):
            if (x == len(strs[j])):
               return strs[0][0:x]
            if prev[x] != strs[j][x]:
               return strs[0][0:x]
      x += 1
   return strs[0][0:x]
    