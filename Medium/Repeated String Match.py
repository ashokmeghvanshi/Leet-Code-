class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        
        ans=0
        t=a
        x=ceil(len(b)/len(a))
        if set(b).issubset(set(a)):
            t=a*x
            ans=ans+x
            while ans<=x+2:
                if b in t or b==t:
                    return ans
                t+=a
                ans+=1   
        return -1
    
