def isValidBST(root):
   def isBST(curr, low, high):
      if (not curr): return True
      
      if (low != None and curr.val <= low or curr.val >= high): 
         return False
      
      return isBST(curr.left, curr.val, high) and isBST(curr.right, low, curr.val)
   
   return isBST(root, None, None)