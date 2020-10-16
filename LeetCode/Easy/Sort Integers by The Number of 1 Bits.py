class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        
        t={}
        for i in arr:
            b=bin(i)[2:].count('1')
            if b not in t:
                t[b]=[i]
            else:
                t[b].append(i)
        result=[]
        for j in sorted(t.keys()):
            result=result+sorted(t[j])
        return result
            
