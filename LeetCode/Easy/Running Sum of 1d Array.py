class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        t=[]
        s=0
        for i in nums:
            s=s+i
            t.append(s)
        return t
