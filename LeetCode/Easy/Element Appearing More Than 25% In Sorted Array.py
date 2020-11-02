class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        d={}
        for i in arr:
            if i not in d:
                d[i]=1
            else:
                d[i]=d[i]+1
        m=max(d.values())
        for i in arr:
            if d[i]==m:
                return i 
