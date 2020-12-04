class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        l=0
        for i in words:
            t=0
            for j in i:
                if j in chars and i.count(j)<=chars.count(j):
                    t=t+1
            if t==len(i):
                l=l+len(i)
        return l
