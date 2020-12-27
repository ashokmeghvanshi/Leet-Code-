class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        cs=0
        i=0
        while i<len(nums):
            s=1
            j=i+1
            p=nums[i]
            while j<len(nums):
                if p<nums[j]:
                    s=s+1
                    p=nums[j]
                else:
                    break
                j=j+1
                
            if s>cs:
                cs=s
                i=i+s
            else:
                i=i+1
        return cs
        
            
