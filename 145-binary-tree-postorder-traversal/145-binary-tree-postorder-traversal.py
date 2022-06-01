# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        arr = []
        curr = root
        while curr!=None:
            if curr.right:
                prev = curr.right
                while prev.left != None and prev.left !=curr:
                    prev = prev.left
                    
                    
                if prev.left == None:
                    prev.left = curr
                    arr.append(curr.val)
                    curr = curr.right
                    
                if prev.left == curr:
                    prev.left = None
                    curr = curr.left
                    
            else:
                
                arr.append(curr.val)
                curr = curr.left
                
        return arr[::-1]