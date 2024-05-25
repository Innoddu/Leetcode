import heapq
class kthLargest:

    def __init__(self, k: int, nums: int):
        self.minHeap, self.k = nums, k
        # change list to heap (min heap)
        # Root node is the smallest value
        heapq.heapify(self.minHeap)

        while len(self.minHeap) > k:
            # Pop smallest value (root node)
            heapq.heappop(self.minHeap)
        

    def add(self, val: int):
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]
            