class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        s=A.split()+B.split()
        t=list(dict.fromkeys(s))
        p=[]
        for i in t:
            if s.count(i)==1:
                p.append(i)
        return p 
        
