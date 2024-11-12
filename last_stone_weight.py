class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        #each step, choose two heaviest stones
        #if x == y, remove both stones
        #if x < y, remove x, y = y - x
        #use maxHeap, pick first two elements, and then modify them
        #repeat until len(maxHeap) == 0, 1
        #easy way to max max heap is to negate all values

        maxHeap = []
        for stone in stones:
            maxHeap.append(-1 * stone)

        heapq.heapify(maxHeap)

        while len(maxHeap) > 1:
            y = -heapq.heappop(maxHeap)
            x = -heapq.heappop(maxHeap)

            if y == x: continue
            if y > x: heapq.heappush(maxHeap, -1 * (y-x))
        
        if maxHeap: return -1 * heapq.heappop(maxHeap)
        else: return 0
