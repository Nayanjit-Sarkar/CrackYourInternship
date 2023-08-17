class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left,right  = 0, 1
        maxp = 0
        while right<len(prices):
            if prices[right] > prices[left]:
                prft = prices[right] - prices[left]
                maxp = max(prft, maxp)
            else:
                left = right
            right+=1



        return maxp