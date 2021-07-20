class Solution:
    def minOperations(self, s: str) -> int:
        
        a,b='',''
        for i in range(len(s)):
            if i%2==0:
                a=a+'0'
                b=b+'1'
            else:
                a=a+'1'
                b=b+'0'
        
        c1,c2=0,0
        for i in range(len(s)):
            if s[i]==a[i]:
                c1=c1+1
            if s[i]==b[i]:
                c2=c2+1
            
        return min(c1,c2)
