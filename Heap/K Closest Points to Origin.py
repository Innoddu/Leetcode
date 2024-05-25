# 973. K Closest Points to Origin    
import heapq
def kClosest(self, points):
    minHeap = []
    for x, y in points:
        dist = ( x ** 2 + (y ** 2) )
        minHeap.append([dist, x, y])

    heapq.heapify(minHeap)
    
    res = []
    while k > 0:
        dist, x, y = heappop(minHeap)
        res.append([x,y])
        k -= 1
    return res
    