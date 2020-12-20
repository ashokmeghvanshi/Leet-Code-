class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 0
        n=sorted(nums)
        if n[-2]*2>n[-1]:
            return -1
        else:
            return nums.index(n[-1])
