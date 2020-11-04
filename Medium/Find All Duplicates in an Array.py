class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        d={}
        for i in nums:
            if i not in d:
                d[i]=1
            else:
                d[i]=d[i]+1
        t=[]
        for i in d:
            if d[i]>1:
                t.append(i)
        return t
