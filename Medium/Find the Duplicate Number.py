class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        t=list(dict.fromkeys(nums))
        for i in t:
            if nums.count(i)>1:
                return i
            
