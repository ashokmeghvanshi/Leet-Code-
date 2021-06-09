class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        
        t=list(dict.fromkeys(nums))
        
        ans=0
        for i in t:
            if nums.count(i)==1:
                ans=ans+i
        
        return ans
