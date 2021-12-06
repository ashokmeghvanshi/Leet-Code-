class Solution:
    def replaceDigits(self, s: str) -> str:
        
        def shift(s1,n1):
            return chr(ord(s1)+n1)
        
        ans=''
        for i in range(1,len(s)+1,2):
            ans=ans+s[i-1]
            if i<len(s):
                ans=ans+shift(s[i-1],int(s[i]))
        
        return ans
