class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        t=list(dict.fromkeys(nums))
        print(t)
        if len(t)!=len(nums):
            return True
        else:
            return False
