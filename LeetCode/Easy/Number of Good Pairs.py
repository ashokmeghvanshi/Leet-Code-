class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        s=0
        for i in range(len(nums)-1):
            if nums[i] in nums[i+1:]:
                s=s+nums[i+1:].count(nums[i])
        return s
                
