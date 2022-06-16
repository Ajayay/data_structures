# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        if root != None:
            curr = root
            arr = []
            while curr!=None:
                if curr.left:
                    prev = curr.left
                    while prev.right != None and prev.right != curr:
                        prev=prev.right
                        
                    if prev.right == None:
                        prev.right = curr
                        curr = curr.left
                    
                    if prev.right == curr:
                        prev.right = None
                        arr.append(curr.val)
                        curr = curr.right
                        
                else:
                    arr.append(curr.val)
                    curr = curr.right
            
            return arr
                        
        
        