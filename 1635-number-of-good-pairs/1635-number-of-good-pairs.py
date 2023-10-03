from collections import Counter
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count, ans = Counter(nums), 0
        for c in count.values():
            if c>1:
                ans+= c*(c-1)//2
        return ans