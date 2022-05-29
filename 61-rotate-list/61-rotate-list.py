# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None:
            return head
        dummy = ListNode(0)
        dummy.next = head
        fast =  dummy
        slow = dummy
        size = self.size(head)
        k = k%size
        for i in range(k):
            if fast != None:
                fast =fast.next
            
        while fast.next != None:
            # print(fast.val)
            slow = slow.next
            fast = fast.next
        
        temp = slow.next
        temp = self.rev(temp)
        slow.next = None
        while temp!= None:
            curr = temp.next
            temp.next = head
            head = temp
            temp = curr
            dummy.next = head
            
        return dummy.next
    
    def size(self,head):
        count = 0
        cur = head
        while cur!=None:
            cur = cur.next
            count+=1
            
        return count
    
    def rev(self,temp):
        
        prev = None
        curr = temp
        
        while curr!=None:
            nex = curr.next
            curr.next = prev
            prev = curr
            curr = nex
            
        return prev