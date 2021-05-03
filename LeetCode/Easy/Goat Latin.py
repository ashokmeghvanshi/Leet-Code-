class Solution:
    def toGoatLatin(self, S: str) -> str:
        
        s=S.split()
        ans=''
        v=['a','e','i','o','u','A','E','I','O','U']
        #print(s)
        k=1
        for i in s:
            res=''
            if i[0] in v:
                res=res+i+'ma'
            else:
                if len(i)==1:
                    res=res+i+'ma'
                else:
                    res=res+i[1:]+i[0]+'ma'
            #print(res)
            res=res+'a'*(k)
            ans=ans+res+' '
            k=k+1
        ans=ans[:-1]
        return ans
