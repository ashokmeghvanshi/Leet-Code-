class Solution:
    def minMoves(self, nums: List[int]) -> int:
        
        nums=sorted(nums)
        
        ans=0
        i=len(nums)-1
        
        while i>-1:
            ans=ans+nums[i]-nums[0]
            i=i-1
            
        return ans
    
#         This solution gives TLE

#         if len(dict.fromkeys(nums))==1:
#             return 0
        
#         #print(nums)
#         ans=0
#         while len(dict.fromkeys(nums))!=1:
            
#             nums=sorted(nums)
#             for i in range(len(nums)-1):
#                 nums[i]=nums[i]+1
            
#             #print(nums)
#             ans=ans+1
        
#         return ans
            
        
