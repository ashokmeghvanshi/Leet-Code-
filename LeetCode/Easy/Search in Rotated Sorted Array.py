class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n=sorted(nums)
        if target<n[0]:
            return -1
        else:
            for i in n:
                if i==target:
                    return nums.index(target)
                if i>target:
                    return -1
            return -1
