class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        
        ans=''
        
        for i in range(len(words)):
            if len(ans)!=len(s):
                ans=ans+words[i]
            
        if ans==s:
            return True
        else:
            return False 
            
