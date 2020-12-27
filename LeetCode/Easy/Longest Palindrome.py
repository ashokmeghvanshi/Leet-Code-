class Solution:
    def longestPalindrome(self, s: str) -> int:
        
        if s==s[::-1]:
            return len(s)
        
        d={}
        for i in s:
            if i not in d:
                d[i]=1
            else:
                d[i]=d[i]+1
        print(d)
        a,b,c=0,0,0
        for i in d:
            if d[i]%2==0:
                a=a+d[i]
            elif d[i]%2!=0 and d[i]!=1:
                a=a+d[i]-1
                c=c+1
            elif d[i]==1 and b==0:
                a=a+d[i]
                b=b+1
        if b==0 and c!=0:
            return a+1
        elif (c==0 and b==0) or (c==0 and b!=0) or (c!=0 and b!=0):
            return a
            
        
