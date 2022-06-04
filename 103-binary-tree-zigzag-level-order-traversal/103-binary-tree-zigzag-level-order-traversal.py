# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if root != None:
            
            q = []
            q.append(root)
            ans = []
            c = 0
            while len(q):
                n = len(q)
                temp = []
                # c = 0
                for i in range(n):
                    node = q.pop(0)
                    
                    temp.append(node.val)
                        
                    if node.left:
                        q.append(node.left)
                        
                    if node.right:
                        q.append(node.right)
                print(temp)
                if c%2 == 0:
                    ans.append(temp)
                else:
                    ans.extend([temp[::-1]])
                    # for i in range(-1,len(temp)-1,-1):
                    #     ans.append(temp[i])

                c+=1
            return ans
                    