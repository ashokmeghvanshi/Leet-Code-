class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        
        # O(N**2)
#         ans=-1
#         for i in range(len(nums)):
#             for j in range(i+1,len(nums)):
                
#                 if nums[i]<nums[j]:
#                     ans=max(ans,nums[j]-nums[i])
#         return ans
        
    
        # O(N)
        max_diff=-1
        
        min_ele=nums[0]
        
        for i in range(1,len(nums)):
            
            if (nums[i]-min_ele)>max_diff:
                max_diff=nums[i]-min_ele
            
            if nums[i]<min_ele:
                min_ele=nums[i]
                
        if max_diff>0:
            return max_diff
        
        else:
            return -1
