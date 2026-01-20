# Middle of the linked list
def middleNode(self, head):
   slow = head 
   fast = head
   while fast != None and fast.next != None:
      slow = slow.next
      fast = fast.next.next
   return slow
     
def middle_node(head):
   arr = []
   curr = head
   while curr.next != None:
      arr.append(curr.val)
      curr = curr.next
   
   middle = len(arr) // 2
   return arr[middle] if len(arr) % 2 == 0 else arr[middle:]