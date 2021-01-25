class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums=sorted(nums)
        a=nums[-2]
        b=nums[-1]
        return (a-1)*(b-1)
