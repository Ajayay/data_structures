# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head is not None:
            fast = head
            slow = head
            if head.next:
                while fast.next.next is not None and fast.next.next.next is not None:
                    slow = slow.next
                    fast = fast.next.next
                slow.next = slow.next.next
            else:
                head = None
            
        return head
                
            