class Solution:
    def minOperations(self, nums: List[int]) -> int:
        
        ans=0
        temp=nums[0]
        for i in range(1,len(nums)):
            if nums[i]<=temp:
                ans=ans+temp-nums[i]+1
                nums[i]=nums[i-1]+1
            
            temp=nums[i]
        #print(nums)
        return ans
