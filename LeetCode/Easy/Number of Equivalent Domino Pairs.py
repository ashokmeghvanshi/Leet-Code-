class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        s=0
        d={}
        for i in dominoes:
            key=str(sorted(i))
            if key in d:
                s=s+d[key]
                d[key]=d[key]+1
                
            else:
                d[key]=1
        return s
