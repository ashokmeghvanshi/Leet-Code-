class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        
        d={}
        for i in range(1,N+1):
            d[i]=0
        #print(d)
        for i in trust:
            a,b=i[0],i[1]
            d[b]=d[b]+1
            d[a]=d[a]-1
        #print(d)
        for i in d:
            if d[i]==N-1:
                return i
        return -1
