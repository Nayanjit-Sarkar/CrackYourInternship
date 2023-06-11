class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        maxL,l= height[0],0
        maxR,r = height[-1], len(height) - 1
        while l<r:
            if maxL<=maxR:
                l+=1
                maxL = max(maxL,height[l])
                ans+=maxL-height[l]
                
            else:
                r-=1
                maxR = max(maxR, height[r])
                ans+=maxR-height[r]
                
        return ans