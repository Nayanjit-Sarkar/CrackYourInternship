class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        k = len(nums)//3
        ans = []
        for val, c in count.items():
            if c > k:
                ans.append(val)
        return ans
