class Solution:
    def reformat(self, s: str) -> str:
        
        alp=[]
        num=[]
        for i in s:
            if i.isalpha()==True:
                alp.append(i)
            else:
                num.append(i)
        #print(alp,num)
        ans=''
        if len(num)==len(alp):
            for i in range(len(num)):
                ans=ans+num[i]+alp[i]
        elif len(num)==len(alp)+1:
            ans=ans+num[0]
            for i in range(len(alp)):
                ans=ans+alp[i]+num[i+1]
        elif len(num)+1==len(alp):
            ans=ans+alp[0]
            for i in range(len(num)):
                ans=ans+num[i]+alp[i+1]
        
        return ans
