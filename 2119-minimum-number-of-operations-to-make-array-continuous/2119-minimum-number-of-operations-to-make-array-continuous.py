class Solution:
    def minOperations(self, nums: List[int]) -> int:
        length = len(nums)
        nums = sorted(set(nums))
        r = 0
        res = length
        for l in range(length):

            while r < len(nums) and nums[r] < nums[l] + length:
                r+=1
            window = r - l 
            res = min(res , length - window)

        return res