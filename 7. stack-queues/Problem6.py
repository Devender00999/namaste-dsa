# You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.
# Evaluate the expression. Return an integer that represents the value of the expression.

# Input: tokens = ["2","1","+","3","*"]
# Output: 9

from typing import List


class Solution:
   def calculate(self, op1, op2, operator):
      if operator == '+':
         return op1 + op2
      if operator == '-':
         return op1 - op2
      if operator == '*':
         return op1 * op2
      else:
         return int(op1 / op2)

   # T(n): O(1); S(n): O(1)
   def evalRPN(self, tokens: List[str]) -> int:
      st = []
      for i in tokens:
         if i in ['+', '-', '/', '*']:
            op2 = st.pop()
            op1 = st.pop()
            # st.append(str(int(self.calculate(op1, op2, i))))
            st.append(str(int(eval(op1 + i + op2))))
         else:
            st.append(i)
      return (int(st.pop()))