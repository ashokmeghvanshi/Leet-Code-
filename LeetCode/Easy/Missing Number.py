class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        m=len(nums)
        s=(m*(m+1))//2
        
        return s-sum(nums)
    
        # for i in nums:
        #     s=s-i
        # return s
        
