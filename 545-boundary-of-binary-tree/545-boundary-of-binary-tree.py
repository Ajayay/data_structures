# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        
        if root!=None:
            res = []
            if self.isLeaf(root) == False:
                res.append(root.val)
            self.leftView(root,res)
            self.bottomView(root,res)
            self.rightView(root,res)
            return res
    
    def isLeaf(self,node):
        if node!= None:
            if node.left == None and node.right == None:
                return True
            return False
        
    def leftView(self,root,res):
        curr = root.left
        
        while curr!=None:
            if self.isLeaf(curr) == False:
                res.append(curr.val)
            if curr.left:
                curr = curr.left
            else:
                curr = curr.right
                
    
    def rightView(self,root,res):
        curr = root.right
        temp = []
        while curr!=None:
            if self.isLeaf(curr) == False:
                temp.append(curr.val)
            if curr.right:
                curr = curr.right
            else:
                curr = curr.left
        res.extend(temp[::-1])
        
    
    def bottomView(self,root,res):
        if self.isLeaf(root):
            res.append(root.val)
            return
        if root.left:
            self.bottomView(root.left,res)
        if root.right:
            self.bottomView(root.right,res)