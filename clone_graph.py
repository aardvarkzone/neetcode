"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        dictionary = {}
        def dfs(node): 
            if node in dictionary: return dictionary[node]
        
            nodeCopy = Node(node.val)
            dictionary[node] = nodeCopy

            for neighbor in node.neighbors: 
                nodeCopy.neighbors.append(dfs(neighbor))

            return nodeCopy

        return dfs(node) if node else None
