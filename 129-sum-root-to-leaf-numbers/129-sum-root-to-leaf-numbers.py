# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        arr = []
        sumVal  = ""
        c = 0
        ans,sumVal,c = self.__help(root, sumVal, arr,c)
        # print(arr)
        return sum(arr)
        
        
    def __help(self, root, sumVal,ans,c):
        if root != None:
            sumVal+=str(root.val)
            
            if root.left:
                ans,sumVal,c = self.__help(root.left, sumVal, ans,c)    
            else:
                c+=1
                
            
            if root.right:
                ans,sumVal,c = self.__help(root.right,sumVal,ans,c)
            else:
                c+=1
                
            
            if c >1:
                ans.append(int(sumVal))
                c = 0
            else:
                c = 0
            
            sumVal = sumVal[:len(sumVal)-1]
                
            return ans,sumVal,c
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
            
            