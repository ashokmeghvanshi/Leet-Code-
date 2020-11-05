class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        t=[]
        for i in words:
            for j in words:
                if i in j and i!=j:
                    t.append(i)
                    break
        return t
