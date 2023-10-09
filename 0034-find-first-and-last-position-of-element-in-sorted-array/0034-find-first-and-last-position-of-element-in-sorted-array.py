class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        ans = [-1, -1]
        l, r = 0, n-1 
        while l<=r:
            if target == nums[l] and target == nums[r]:
                ans = [l , r]
                break
                
            if target > nums[l]:
                l +=1
            if target < nums[r]:
                r -=1
            
        return  ans
        

