# Given an array of strings strs, group the anagrams together.
# You can return the answer in any order.

# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

# T(n): O(n); S(n): O(1)
def isAnagram(s, t):
   if len(s) != len(t):
      return False
   
   keys = { }
   for key in s:
      if key in keys:
            keys[key] += 1
      else:
            keys[key] = 1

   for key in t:
      if key in keys:
            keys[key] -= 1
      else:
            keys[key] = -1

   for key in keys.keys():
      if keys[key] != 0:
            return False
            
   return True 

# T(n): O(n^2*m); S(n): O(n)
# m: length of string
def groupAnagrams(strs):
   group = []
   visited = set()
   for i in range(len(strs)): # n
         if strs[i] in visited:
            continue
         cgroup = [strs[i]]
         visited.add(strs[i])
      
         for j in range(i + 1, len(strs)): # n
            if isAnagram(strs[i], strs[j]): # m
               cgroup.append(strs[j])
               visited.add(strs[j])
               visited.add(strs[i])
         group.append(cgroup)
   return group 

# T(n): O(n * mlogm); S(n): O(n * m)
# m: length of the string
def groupAnagrams(strs):
   mapping = {}
   for i in range(len(strs)):
      key = "".join(sorted(strs[i]))
      if key in mapping:
            mapping[key].append(strs[i])
      else:
            mapping[key] = [strs[i]]
   return mapping.values()


# T(n): O(n * m); S(n): O(n * m)
# m: length of the string
def groupAnagrams(strs):
   mapping = {}
   for i in range(len(strs)):
      freq_arr = [0] * 26
      for char in strs[i]:
            keyIdx = ord(char) - ord('a')
            freq_arr[keyIdx] += 1
      key = ""
      
      for key_char in range(len(freq_arr)):
            key += chr(key_char + ord('a')) + str(freq_arr[key_char])
               
      if key in mapping:
            mapping[key].append(strs[i])
      else:
            mapping[key] = [strs[i]]
   return mapping.values()

