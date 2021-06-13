class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s)==len(t):
            l=list(dict.fromkeys(t))
            a=0
            for i in l:
                if s.count(i)==t.count(i):
                    a=a+1
            if a==len(l):
                return True
            else:
                return False
        else:
            return False
