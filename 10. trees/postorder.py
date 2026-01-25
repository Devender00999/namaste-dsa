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

def postorderTraversal(root: TreeNode, arr: List[int]):
   if not root:
      return arr
   postorderTraversal(root.left, arr)
   postorderTraversal(root.right, arr)
   arr.append(root.val)
   return arr

def postOrderTraversalIterative(root: TreeNode):
   if not root: return
   s1 = [root]
   s2 = []
   while (len(s1)):
      curr = s1.pop()   
      s2.append(curr)
      if curr.left: s1.append(curr.left)
      if curr.right: s1.append(curr.right)
   
   ans = []
   while len(s2):
      ans.append(s2.pop().val)
   return ans
   
print(postorderTraversal(root, []))
print(postOrderTraversalIterative(root))