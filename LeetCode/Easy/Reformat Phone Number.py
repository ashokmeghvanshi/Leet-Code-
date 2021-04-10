class Solution:
    def reformatNumber(self, number: str) -> str:
        
        s=''
        for i in number:
            if i.isdigit()==True:
                s=s+i
        r=len(s)%3
        
        ans=""
        if r==0:
            for i in range(0,len(s),3):
                ans+=s[i:i+3]+"-"        
            ans=ans[:-1]
            #return ans
        
        elif r==1:
            #print(s)
            for i in range(0,len(s)-3,3):
                ans+=s[i:i+3]+"-"
            #print(ans)
            t=ans[-2:]
            #print(t)
            ans=ans[:-2]+t[::-1]+s[-1]
            #print(ans)
        
        elif r==2:
            #print(s)
            for i in range(0,len(s)-3,3):
                ans+=s[i:i+3]+"-"
            #print(ans)
            ans=ans+s[-2:]
            #print(ans)
        return ans
