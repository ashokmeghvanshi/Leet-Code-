class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        
        s=0
        for i in words:
            t=0
            for j in i:
                if j in allowed:
                    pass
                else:
                    break
                t=t+1
            if t==len(i):
                s=s+1
        return s
                
