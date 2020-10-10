class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        t=[]
        for i in queries:
            ms=i.count(min(i))
            s=0
            for j in words:
                mw=j.count(min(j))
                if mw>ms:
                    s=s+1
            t.append(s)
                
        return t
        
