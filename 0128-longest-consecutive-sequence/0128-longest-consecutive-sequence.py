class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) in [0,1]:
            return len(nums)
        l = sorted(nums)
        res = c = 1
        for i in range(1,len(l)):
            if (l[i] - l[i-1]) == 1:
                c+=1 
            elif (l[i] - l[i-1]) != 0 :
                c = 1
            res = max(res, c)
        return res

        