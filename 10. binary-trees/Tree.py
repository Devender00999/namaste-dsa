from preorder import preorderTraversal
class TreeNode():
   def __init__(self, val = 0, left = None, right = None):
      self.val = val
      self.left = left 
      self.right = right
   
   
   def generateTree(arr: list):
      if len (arr) == 0: return None
      q = [arr[0]]
      length = len(arr)
      i = 0
      tree = None
      while (i < length):
         curr = q.pop(0)
         if (tree == None):
            node = TreeNode(curr)
            i += 1;
            if (i < length):
               node.left = TreeNode(arr[i])
      
     
         
      #      1
      #     2 3
      #   4  5  6 7
      #  8 9 

