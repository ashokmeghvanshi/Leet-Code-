class Solution:
    def makeFancyString(self, s: str) -> str:
        
        ans=''
        if len(s)<3:
            return s
        else:
            ans=s[:2]
            for i in range(2,len(s)):
                if ans[-1]!=s[i] or ans[-2]!=s[i]:
                    ans=ans+s[i]
        #print(ans)
        return ans
        
