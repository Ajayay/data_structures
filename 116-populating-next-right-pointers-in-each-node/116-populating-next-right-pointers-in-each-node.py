"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        
        if root is not None:
            lmost = root
            while lmost.left is not None:
                head = lmost
                while head != None:
                    head.left.next = head.right
                    if head.next:
                        head.right.next = head.next.left
                    head = head.next
                    
                lmost = lmost.left
        
            return root