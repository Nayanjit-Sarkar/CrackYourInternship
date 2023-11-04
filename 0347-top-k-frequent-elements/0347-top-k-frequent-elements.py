from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = []
        hashmap = dict()
        freq = [[] for i in range(len(nums) + 1)]
        for i in nums:
            hashmap[i] = 1 + hashmap.get(i , 0)
            
        for n,f in hashmap.items():
            freq[f].append(n)
        
        for j in range(len(freq)-1, 0, -1):
            if len(freq[j]) > 0:
                ans.extend(freq[j])
            if len(ans) == k:
                return ans


        