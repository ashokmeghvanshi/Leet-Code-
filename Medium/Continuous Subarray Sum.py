class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        
        if not nums:
            return False
        dp={0:-1}
        s=0
        for i in range(len(nums)):
            s=s+nums[i]
            if k!=0:
                s=s%k
            if s in dp:
                if i-dp[s]>=2:
                    return True
            else:
                dp[s]=i
        return False
    
