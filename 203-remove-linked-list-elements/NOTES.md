```
if head:
dummy = ListNode(0,head)
curr = dummy
while curr.next != None:
if curr.next.val ==val:
curr.next =curr.next.next
cur = curr.next
if dummy.next:
return dummy.next
else:
dummy.next  = None
return dummy.next
```