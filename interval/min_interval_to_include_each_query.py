import heapq
# 1851. Minimum Interval to Include Each Query
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort(key=lambda x:x[0])
        minHeap = []
        res, i = {}, 0
        for q in sorted(queries):
            while i < len(intervals) and intervals[i][0] <= q:
                start, end = intervals[i]
                heapq.heappush(minHeap, (end - start + 1, end))
                i += 1
            
            while minHeap and minHeap[0][1] < q:
                heapq.heappop(minHeap)
            res[q] = minHeap[0][0] if minHeap else -1

        return [res[q] for q in queries]




