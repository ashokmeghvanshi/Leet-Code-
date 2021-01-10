class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        ans=0
        i=0
        nums=sorted(nums)
        while i<len(nums)-1:
            ans=ans+min(nums[i],nums[i+1])
            i=i+2
        return ans
