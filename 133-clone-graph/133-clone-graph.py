"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    
    def __init__(self):
        self.vis = {}
    
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node is None:
            return node
        
        if node in self.vis:
            return self.vis[node]
        else:
            cloned_node = Node(node.val,[])
            self.vis[node] = cloned_node
            if node.neighbors:
                for j in node.neighbors:
                    cloned_node.neighbors.append(self.cloneGraph(j))
                    
        return cloned_node
        
        