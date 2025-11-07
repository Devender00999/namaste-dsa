# Given two strings s and t, determine if they are isomorphic.
# Two strings s and t are isomorphic if the characters in s can be replaced to get t.
# All occurrences of a character must be replaced with another character while preserving the order of characters. 
# No two characters may map to the same character, but a character may map to itself.

# Input: s = "egg", t = "add"
# Output: true

# T(n): O(n); S(n): O(1) 
def isIsomorphic(s, t):
   if len(s) != len(t): return False
   
   mapStoT = {}   
   mapTtoS = {}
   
   for i in range(len(s)):
      if s[i] in mapStoT and mapStoT[s[i]] != t[i]:
         return False
      else:
         mapStoT[s[i]] = t[i]
         
   for i in range(len(t)):
      if t[i] in mapTtoS and mapTtoS[t[i]] != s[i]:
         return False
      else:
         mapTtoS[t[i]] = s[i]
   
   return True

print(isIsomorphic('egg', 'add'))
print(isIsomorphic('baba', 'bada'))
      