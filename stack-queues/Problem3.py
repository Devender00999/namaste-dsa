# Valid Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# Input: s = "()"
# Output: true

def isValid(s: str) -> bool:
   stack = []
   for i in range(len(s)):
      if (len(stack) == 0):
            stack.append(s[i])
      else:
            top = stack[len(stack) - 1]
            if (top == '(' and s[i] == ')'):
               stack.pop()
            elif (top == '[' and s[i] == ']'):
               stack.pop()
            elif (top == '{' and s[i] == '}'):
               stack.pop()
            else:
               stack.append(s[i])
   return True if len(stack) == 0 else False

def isValid(s: str) -> bool:
   stack = []
   for i in s:
      if i == "(" or i == "[" or i == '{':
         stack.append(i)
      else:
         top = stack.pop()
         if (not top or top == '(' and i != ')' or top == '[' and i != ']' or top == '{' and i != '}'):
            return False
   return True

def isValid(s: str) -> bool:
   stack = []
   map = { '(': ")", "{": "}", '[': "]"}
   for i in s:
      if map.get(i) != None:
            stack.append(i)
      else:
            if len(stack) == 0: return False
            top = stack.pop()
            if (map[top] != i):
               return False
   return len(stack) == 0     
