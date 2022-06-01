# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        arr = []
        q = []
        q.append(root)
        while len(q)>0:
            n = len(q)
            temp =[]
            for i in range(1,n+1):
                node = q.pop()
                if node != None:
                    temp.append(node.val)
                    if node.left:
                        q.insert(0,node.left)

                    if node.right:
                        q.insert(0,node.right)
            if len(temp) > 0:        
                arr.append(temp)
        
        return arr