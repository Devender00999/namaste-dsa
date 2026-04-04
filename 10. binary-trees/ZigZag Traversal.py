from Tree import TreeNode

def levelOrderWithArray(root: TreeNode):
   if not root: return ans
   ans = [], q1 = [root], level = 0
   while len(q1):
      levelArr = []
      for i in range(len(q1)):
         curr = q1.pop(0)
         if (level % 2 == 0): levelArr.append(curr.val)
         else: levelArr.insert(0, curr.val)
         curr.left and q1.append(curr.left)
         curr.right and q1.append(curr.right)
      ans.append(levelArr)
   return ans

