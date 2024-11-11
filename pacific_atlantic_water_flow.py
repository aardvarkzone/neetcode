from collections import deque
from typing import List, Set, Tuple

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        #graph theory
        #solve using BFS but start at the edges and try and work inwards
        #see if neighboring cells are taller or equal 
        #get the edges
        #need to do bfs twice, and then and the two sets 
        #edges becomes reachable

        output = []
        if not heights: return output
        
        rows = len(heights)
        cols = len(heights[0])

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        pac_set = set()
        atl_set = set()
        
        for row in range(rows): 
            pac_set.add((row, 0))
            atl_set.add((row, cols - 1))
        
        for col in range(cols):
            pac_set.add((0, col))
            atl_set.add((rows - 1, col))

        def bfs(edges: Set[Tuple[int,int]], reachable: Set[Tuple[int,int]]): 
            queue = collections.deque(edges)
            while queue: 
                row, col = queue.popleft()
                for change_row, change_col in directions: 
                    new_row = change_row + row
                    new_col = change_col + col
                    if 0 <= new_row < rows and\
                       0 <= new_col < cols and\
                       (new_row, new_col) not in reachable: 
                        if heights[new_row][new_col] >= heights[row][col]:
                            queue.append((new_row, new_col))
                            reachable.add((new_row, new_col))
        
        bfs(pac_set, pac_set)
        bfs(atl_set, atl_set)
        output = list(pac_set & atl_set)
        return output 
