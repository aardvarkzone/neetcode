class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        #undirected graph
        #0 to n-1
        #create adj list
        #create visited set
        #from vertex 0 to n-1, if its not visited already, new component and dfs
        
        components = 0
        adjList = defaultdict(list)
        
        for a, b in edges:
            adjList[a].append(b)
            adjList[b].append(a)
        
        visited = set()

        def dfs(vertex):
            visited.add(vertex)

            for neighbor in adjList[vertex]:
                if neighbor not in visited:
                    dfs(neighbor)
            return
        
        for vertex in range(n):
            if vertex not in visited: 
                components += 1
                dfs(vertex)



        return components
