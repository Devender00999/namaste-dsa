from Tree import TreeNode
from typing import Optional

def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
   if not root: return False
   ans = False

   def traverse(curr, currSum):
      newSum = currSum + curr.val
      nonlocal ans
      if not curr.left and not curr.right:
            if newSum == targetSum:
               ans = ans or True
      curr.left and traverse(curr.left, newSum)
      curr.right and traverse(curr.right, newSum)
   traverse(root, 0)
   return ans

def traverse(self, curr, targetSum, currSum):
   if not curr.left and not curr.right:
      if targetSum == currSum + curr.val:
            return True
      return False
   pathSumLeft = False
   if curr.left:
      pathSumLeft = self.traverse(curr.left, targetSum, currSum + curr.val)
   pathSumRight = False
   if curr.right:
      pathSumRight = self.traverse(curr.right, targetSum, currSum + curr.val)
   return pathSumRight or pathSumLeft

def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
   if not root: return False
   if not root.left and not root.right:
      return root.val == targetSum
   hasLeftSum = self.hasPathSum(root.left, targetSum - root.val)
   hasRightSum = self.hasPathSum(root.right, targetSum - root.val)

   return hasLeftSum or hasRightSum
