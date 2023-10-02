import heapq as hq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [i*-1 for i in stones]
        hq.heapify(stones)
        while len(stones)>1:
            x = hq.heappop(stones)
            y = hq.heappop(stones)
            if y>x:
                hq.heappush(stones, x-y)
        if stones:
            return -hq.heappop(stones)
        return 0
        