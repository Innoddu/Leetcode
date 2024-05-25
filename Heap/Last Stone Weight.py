import heapq
# 1046. Last Stone Weight
def lastStoneWeight(stones):
        stones = [-stone for stone in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            x = heapq.heappop(stones)
            y = heapq.heappop(stones)
            x = -x
            y = -y
            if x == y:
                heapq.heappush(stones, 0)
            if x != y:
                heapq.heappush(stones, y - x)

            print(x, y)
        return -stones[0]