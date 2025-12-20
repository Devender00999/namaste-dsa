def getIntersectionNode(headA, headB):
   lenA, lenB = 0,0
   curr = headA
   while curr:
      curr = curr.next
      lenA += 1
   
   curr = headB
   while curr:
      curr = curr.next
      lenB += 1

   diff = abs(lenA - lenB)
   if lenA > lenB:
      curr1 = headA
      curr2 = headB
   else:
      curr1 = headB
      curr2 = headA
   while diff > 0:
      curr1 = curr1.next
      diff -= 1
   
   while curr1 != curr2:
      curr1 = curr1.next
      curr2 = curr2.next
   return curr1