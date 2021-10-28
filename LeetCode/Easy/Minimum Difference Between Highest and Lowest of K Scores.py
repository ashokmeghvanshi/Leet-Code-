class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        
        ans=10000000
        
        nums=sorted(nums)
        
        for i in range(len(nums)-k+1):
            
            t=nums[i:i+k]
            mx=max(t)
            mi=min(t)
            #print(t,mx,mi)
            ans=min(ans,mx-mi)
            
        return ans
