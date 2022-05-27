```
def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
if head:
fast= head
slow = head
flag = False
while fast != None and fast.next != None:
slow = slow.next
fast = fast.next.next
if fast == slow:
flag = True
if flag:
dummy = head
count = 0
while slow != None and slow.next != None:
if dummy == slow:
return count
else:
slow = slow.next
dummy = dummy.next
count+=1
return count
return None
```