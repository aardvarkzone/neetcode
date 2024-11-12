class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #need to return k number of points 
        #use smallest distance -- meaning minHeap 

        dist = []
        for x, y in points:
            dist.append((math.sqrt(x**2 + y**2), [x, y]))
        
        heapq.heapify(dist)

        output = []

        while k:
            distance, point = heapq.heappop(dist)
            output.append(point)
            k -= 1
            
        return output
