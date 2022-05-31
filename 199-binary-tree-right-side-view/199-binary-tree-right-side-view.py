# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        
        if root is not None:
            ans = []
            queue = []
            queue.append(root)
            
            while len(queue)>0:                
                n = len(queue)
                for i in range(1,n+1):
                    node =  queue.pop(0)
                    if i == n:
                        ans.append(node.val)
                    
                    if node.left:
                        queue.append(node.left)
                        
                    
                    if node.right:
                        queue.append(node.right)
                        
                        
            return ans