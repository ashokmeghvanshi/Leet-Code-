class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        
        ans=''
        for i in s.split()[:k]:
            ans=ans+i+' '
        
        return ans[:-1]
