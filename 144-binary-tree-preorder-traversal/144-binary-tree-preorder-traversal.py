# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        arr = []
        self.__preorder(arr, root)
        
        return arr
    
    def __preorder(self,arr,root):
        if root == None:
            return None
        
        arr.append(root.val)
        if root.left:
            self.__preorder(arr,root.left)
            
        if root.right:
            self.__preorder(arr, root.right)