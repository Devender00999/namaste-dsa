from Tree import TreeNode
from typing import Optional

def hasPathSum(root: Optional[TreeNode], targetSum: int) -> bool:
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

def hasPathSum(root: Optional[TreeNode], targetSum: int) -> bool:
   if not root: return False
   if not root.left and not root.right:
      return root.val == targetSum
   hasLeftSum = hasPathSum(root.left, targetSum - root.val)
   hasRightSum = hasPathSum(root.right, targetSum - root.val)

   return hasLeftSum or hasRightSum
