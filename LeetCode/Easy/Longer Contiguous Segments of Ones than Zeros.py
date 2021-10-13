class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        
        ans1=0
        ans0=0
        
        for i in range(len(s)):
            
            if s[i]=='1':
                check1=0
                for j in range(i,len(s)):
                    if s[i]==s[j]:
                        check1=check1+1
                    else:
                        break
                if check1>ans1:
                    ans1=check1
                    
            if s[i]=='0':
                check0=0
                for j in range(i,len(s)):
                    if s[i]==s[j]:
                        check0=check0+1
                    else:
                        break
                if check0>ans0:
                    ans0=check0
        #print(ans0,ans1)
        if ans0<ans1:
            return True
        else:
            return False
