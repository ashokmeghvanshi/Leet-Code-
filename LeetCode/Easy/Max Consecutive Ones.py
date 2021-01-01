class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        s=0
        mx=0
        nums=nums+[0]
        for j in range(len(nums)):
            if nums[j]==1:
                s=s+1
            else:
                mx=max(s,mx)
                s=0
        return mx
