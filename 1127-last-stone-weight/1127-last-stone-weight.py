import heapq as hq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [i*-1 for i in stones]
        hq.heapify(stones)
        while len(stones)>2:
            x = hq.heappop(stones)
            y = hq.heappop(stones)
            if y>x:
                hq.heappush(stones, x-y)
        if len(stones) == 1:
            return stones[0]*-1
        else:
            x = hq.heappop(stones)
            y = hq.heappop(stones)
        return y-x
        