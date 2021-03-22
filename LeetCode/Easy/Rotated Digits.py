class Solution:
    def rotatedDigits(self, N: int) -> int:
        mirrored=['2','5','6','9']
        mirrorednot=['3','7','4']
        ans=0
        check=False
        for i in range(1,N+1):
            for j in str(i):
                if j in mirrored:
                    check=True
                elif j in mirrorednot:
                    check=False
                    break
            if check==True:
                ans=ans+1
                check=False
                
        return ans
