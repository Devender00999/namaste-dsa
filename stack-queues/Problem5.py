class Solution:
   def removeOuterParentheses(self, s: str) -> str:
      stack = []
      ans = ""
      for i in range(len(s)):
         if (s[i] == '('):
               stack.append(s[i])
               if (len(stack) > 1):
                  ans += s[i]
         else:
               if (len(stack) > 1):
                  ans += s[i]
               top = stack.pop()
      return ans