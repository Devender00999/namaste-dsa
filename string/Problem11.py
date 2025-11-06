def isIsomorphic(self, s, t):
   """
   :type s: str
   :type t: str
   :rtype: bool
   """
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