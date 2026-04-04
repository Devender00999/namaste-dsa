from Tree import TreeNode
from typing import Optional

def traverse2(root: TreeNode, depth):
   if not root:
      return depth
   depth1 = traverse2(root.left, depth + 1)
   depth2 = traverse2(root.right, depth + 1)
   return max(depth1, depth2)

# Top down approach
def maxDepthTopDown(root):
   maxDepth = 0
   def traverse2(root: TreeNode, depth):
      maxDepth = max(maxDepth, depth)
      root.left and traverse2(root.left, depth + 1)
      root.right and traverse2(root.right, depth + 1)
   traverse2(root, 1)
   return maxDepth
   
# Bottom up aaproach
def maxDepthBottomUp(root: Optional[TreeNode]) -> int:
   if not root: return 0
   leftMax = maxDepthBottomUp(root.left)
   rightMax = maxDepthBottomUp(root.right)
   return 1 + max(leftMax , rightMax)