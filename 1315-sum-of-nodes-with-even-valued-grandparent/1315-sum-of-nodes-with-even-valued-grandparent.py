# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        count = 0
        node = root
        if root is not None:
            return self.__helper_method(node,None,None)
        
    
    def __helper_method(self, node, parent ,gp):
        sum_val = 0
        if node is None:
            return 0
        if gp!= None and gp.val%2==0:
            sum_val+=node.val
        if node.left:
            sum_val+=self.__helper_method(node.left, node, parent)
        if node.right:
            sum_val+= self.__helper_method(node.right, node, parent)
        return sum_val