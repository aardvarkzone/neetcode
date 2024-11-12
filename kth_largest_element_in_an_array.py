class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #use maxheap
        maxHeap = []
        for num in nums: 
            maxHeap.append(-1 * num)
        
        heapq.heapify(maxHeap)

        for _ in range(k-1):
            heapq.heappop(maxHeap)

        return -1 * maxHeap[0]
