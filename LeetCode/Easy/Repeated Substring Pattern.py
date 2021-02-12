class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
         
        l=len(s)
        for i in range(1,len(s)//2 + 1):
            a=s[:i]
            p=l//len(a)
            a=a*p
            if a==s and l%i==0:
                return True
        return False
    
