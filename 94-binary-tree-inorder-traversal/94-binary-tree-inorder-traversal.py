# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        arr = []
        return self._help(root, arr)
    
    
    def _help(self,root,arr):
        if root is None:
            return 
        self._help(root.left,arr)
        arr.append(root.val)
        self._help(root.right,arr)
        return arr
        
        