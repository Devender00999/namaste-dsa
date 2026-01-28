from Tree import TreeNode
from typing import List

# Example
# Create nodes
node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node6 = TreeNode(6)
node7 = TreeNode(7)
node8 = TreeNode(8)
node9 = TreeNode(9)

# Build the tree
node1.left = node2
node1.right = node3

node2.left = node4
node2.right = node5

node5.left = node6
node5.right = node7

node3.right = node8
node8.left = node9

root = node1

def levelOrderWithArray(root: TreeNode):
   ans = []
   if not root: return ans
   q1 = [root]
   while len(q1):
      levelArr = []
      for i in range(len(q1)):
         curr = q1.pop(0)
         levelArr.append(curr.val)
         curr.left and q1.append(curr.left)
         curr.right and q1.append(curr.right)
      ans.append(levelArr)
   return ans

def levelOrder(root: TreeNode):
   ans = []
   if not root: return ans
   q1 = [root]
   while len(q1):
      curr = q1.pop(0)
      ans.append(curr.val)
      curr.left and q1.append(curr.left)
      curr.right and q1.append(curr.right)
   return ans

def traversal(curr: TreeNode, level, ans):
      if len(ans) == level: ans.append([])
      ans[level].append(curr.val)
      curr.left and traversal(curr.left, level + 1, ans)
      curr.right and traversal(curr.right, level + 1, ans)
      
def levelOrderRecursive(root: TreeNode):
   if not root: return []
   ans = []
   traversal(root, 0, ans)
   return ans
print(levelOrderWithArray(root))
print(levelOrder(root))
print(levelOrderRecursive(root))