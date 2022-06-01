# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        arr = []
        curr = root
        while curr !=None:
            if curr.left:
                # arr.append(curr.val)
                prev = curr.left
                while prev.right != None and prev.right !=curr:
                    prev = prev.right
                    
                if prev.right == None:
                    prev.right = curr
                    arr.append(curr.val)
                    curr=curr.left
                if prev.right == curr:
                    prev.right = None
                    # arr.append(curr.val)
                    curr = curr.right
                    
            else:
                arr.append(curr.val)
                curr = curr.right
        
        return arr
                