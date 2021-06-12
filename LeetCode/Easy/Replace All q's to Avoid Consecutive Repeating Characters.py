class Solution:
    def modifyString(self, s: str) -> str:
        
        ans=''
        ch='abcdefghijklmnopqrstuvwxyz'
        for i in range(len(s)):
            if s[i]=='?' and i==0:
                if len(s)==1:
                    return 'a'
                elif len(s)>1 and s[i+1]!='a':
                    ans=ans+'a'
                elif len(s)>1 and s[i+1]!='b':
                    ans=ans+'b'
            
            elif s[i]=='?' and i!=0 and i!=len(s)-1:
                for j in ch:
                    if s[i+1]!=j and ans[i-1]!=j:
                        ans=ans+j
                        #print('ok',ans,i)
                        break
            
            elif s[i]=='?' and i==len(s)-1:
                for j in ch:
                    if ans[i-1]!=j:
                        ans=ans+j
                        break
            else:
                ans=ans+s[i]
            #print(ans,i)
        return ans
            
                
                
