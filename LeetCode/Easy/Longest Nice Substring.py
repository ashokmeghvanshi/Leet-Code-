class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        
        if len(s)<2:
            return ''
        
        def check(t):
            a=0
            #print(t)
            for i in range(len(t)):
                #print(t[i].lower())
                if t[i].lower()==t[i]:
                    if t[i].upper() in t:
                        a=a+1
                
                if t[i].upper()==t[i]:
                    if t[i].lower() in t:
                        a=a+1
                #print(a)
            if a==len(t):
                return True
            else:
                return False
            
        ans=[]
        for i in range(len(s)-1):
            for j in range(i+1,len(s)):
                if check(s[i:j+1])==True:
                    #print(s[i:j+1])
                    if len(ans)==0:
                        ans.append(s[i:j+1])
                    else:
                        if ans[-1] in s[i:j+1]:
                            ans=ans[:-1]+[s[i:j+1]]
                        else:
                            ans.append(s[i:j+1])
                        
                        
                         
        #print(sorted(ans))
        ans=sorted(ans,key=len)
        if len(ans)!=0:
            if len(ans)==1:
                return ans[-1]
            j=len(ans)-1
            while j>0:
                if len(ans[j])==len(ans[j-1]):
                    pass
                else:
                    return ans[j]
                j=j-1
            return ans[j]
        return ''
