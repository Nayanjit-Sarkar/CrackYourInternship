class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        m = {}
        for n in nums:
            if n in m:
                m[n]+=1
            else:
                m[n] = 1
        freq = sorted(m.items(), key=lambda x:x[1], reverse=True)
        ans = []
        for i in range(k):
            ans.append(freq[i][0])
        return ans