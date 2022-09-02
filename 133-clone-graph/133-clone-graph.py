"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node is None:
            return node
        else:
            # storing {og_node : cloned_node}
            vis = {}
            vis[node] = Node(node.val,[])
            # storing og_nodes in q
            q = []
            q.append(node)
            while q:
                n = q.pop(0)
                for i in n.neighbors:
                    if i not in vis:
                        vis[i] = Node(i.val,[])
                        q.append(i)
                    # get cloned_node from vis in its neighbor add the new cloned neighbor node
                    vis[n].neighbors.append(vis[i])
            return vis[node]