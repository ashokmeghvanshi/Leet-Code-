class Solution:
    def reorderSpaces(self, text: str) -> str:
        
        sl=len(text)
        t=text.split()
        l=len(''.join(t))
        a=(sl-l)
        b=(len(t)-1)
        ans=''
        
        if a!=0 and b!=0:
            if a%b==0:
                total=a//b
                for i in t[:-1]:
                    ans=ans+i+' '*total
                ans=ans+t[-1]
                return ans
            else:
                total1=a//b
                total2=a%b
                for i in t[:-1]:
                    ans=ans+i+' '*total1
                ans=ans+t[-1]+' '*total2
                return ans
                
            #print(total)
        else:
            ans=ans+t[0]+' '*a
            return ans
