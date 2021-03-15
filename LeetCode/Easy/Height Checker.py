class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        
        nums=sorted(heights)
        
        i=0
        result=0
        while i<len(nums):
            if nums[i]!=heights[i]:
                result=result+1
            i=i+1
        return result
