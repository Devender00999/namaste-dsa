# Given two strings s and t, return true 
# if t is an anagram of s, and false otherwise.

# Input: s = "anagram", t = "nagaram"
# Output: true

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

