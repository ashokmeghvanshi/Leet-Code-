class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        d={}
        for i in A:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        
        return max(d,key=d.get)     
