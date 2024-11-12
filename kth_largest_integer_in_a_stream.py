class KthLargest:
    #stream is not always sorted
    #need to use a min heap 
    #heap should be of size k because you only need kth max element 
    #make nums the heap 
    #while size of heap > k, pop min value

    def __init__(self, k: int, nums: List[int]):
        self.k = k 
        self.minHeap = nums
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]
