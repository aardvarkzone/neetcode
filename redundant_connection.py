from typing import Optional
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        #remove extra edge to make valid tree
        #basically remove cycle
        #undirected, connected
        #1 indexed

        #use DFS to find the cycle, if visited 

        def dfs(vertex, root) -> Optional[List[int]]:
            if vertex in visited: 
                #cycle detected
                return [vertex, root]
            visited.add(vertex)
            for neighbor in adjList[vertex]:
                if neighbor != root:
                    result = dfs(neighbor, vertex)
                    if result: return result

        adjList = defaultdict(list)

        for a, b in edges: 
            visited = set()  
            adjList[a].append(b)
            adjList[b].append(a)
            output = dfs(a, a)
            if output: return output

