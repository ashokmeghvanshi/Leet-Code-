class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        
        ans=0
        d={}
        for i in nums:
            if i not in d:
                d[i]=1
            else:
                d[i]=d[i]+1
        #print(d)
        
        for i in d:
            if i+k in d:
                ans=ans+d[i]*d[i+k]
        
        
#         for i in range(len(nums)):
#             for j in range(i,len(nums)):
#                 if abs(nums[i]-nums[j])==k:
#                     ans=ans+1
        
        return ans
