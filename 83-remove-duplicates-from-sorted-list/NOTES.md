```
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
if head is not None:
start = head
second = start.next
​
while start!=None or second!=None:
while start.val == second.val:
second = second.next
start.next = second
second = second.next
start = start.next
​
return head
```