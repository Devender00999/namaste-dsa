
def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
   m = {
      nums2[-1]: -1
   }
   stack = [nums2[-1]]
   n = len(nums2)
   for i in range(len(nums2) - 2, -1, -1):
      top = stack[len(stack) - 1]
      if nums2[i] < top:
            m[nums2[i]] = top
      else:
            while len(stack) > 0:
               top = stack[len(stack) - 1]
               if nums2[i] < top:
                  m[nums2[i]] = top
                  break
               else:
                  stack.pop()
            
            if len(stack) == 0:
               m[nums2[i]] = -1
      stack.append(nums2[i])
      
   for i in range(len(nums1)):
      nums1[i] = m[nums1[i]]
   return nums1