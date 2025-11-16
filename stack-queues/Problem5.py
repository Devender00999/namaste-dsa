# Remove Outermost Parentheses

# Input: s = "(()())(())"
# Output: "()()()"


class Solution:
   # T(n): O(n); S(n): O(n)
   def removeOuterParentheses(self, s: str) -> str:
      stack = []
      ans = ""
      for i in s:
         if i == '(':
            stack.append(i)
            if len(stack) > 1:
               ans += i
         else:
            if len(stack) > 1:
               ans += i
            stack.pop()
      return ans
   
   # T(n): O(n); S(n): O(1)
   def removeOuterParenthesesV2(self, s: str) -> str:
      cnt = 0
      ans = ""
      for i in s:
         if i == '(':
               cnt += 1
               if cnt > 1:
                  ans += i
         else:
               if cnt > 1:
                  ans += i
               cnt -= 1
      return ans
   
   
st = Solution()
print(st.removeOuterParenthesesV2('(()())(())(()(()))'))