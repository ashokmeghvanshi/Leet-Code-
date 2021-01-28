class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        t=list(dict.fromkeys(ransomNote))
        s=0
        for i in t:
            if ransomNote.count(i)<=magazine.count(i):
                s=s+1
        if s==len(t):
            return True
        else:
            return False
