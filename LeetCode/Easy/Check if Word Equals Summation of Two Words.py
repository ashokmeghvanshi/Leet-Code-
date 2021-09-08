class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        
        def check(s):
            ans=''
            for i in s:
                ans=ans+str(ord(i)-97)
            return int(ans)
        
        n1=check(firstWord)
        n2=check(secondWord)
        n3=check(targetWord)
        
        if n1+n2==n3:
            return True
        else:
            return False
