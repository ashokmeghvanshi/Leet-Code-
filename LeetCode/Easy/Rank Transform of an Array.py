class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        
        t=sorted(dict.fromkeys(arr))
        d={}
        for i in range(len(t)):
            d[t[i]]=i+1
        #print(d)
        result=[]
        #print(t)
        for i in arr:
            result.append(d[i])
        return result
