class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l,r = 0,len(nums)-1
        if nums.count(val) == 0:
            return len(nums)
        while l<r:
            if nums[l] == val:
                if nums[r]!=val:
                    nums[l], nums[r] = nums[r], nums[l]
                    
                else:
                    r-=1
                    
            else:
                l+=1
        
        return l