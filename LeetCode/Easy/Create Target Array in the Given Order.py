class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        t=[]
        for i,j in zip(nums,index):
            t.insert(j,i)
        return t
