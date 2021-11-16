class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        
        ans=0
        
        v=['a','e','i','o','u']
        
        for i in range(len(word)):
            for j in range(i,len(word)):
                if len(word[i:j+1])>4:
                    s=0
                    for k in word[i:j+1]:
                        if k in v:
                            s=s+1
                    
                    if s==len(word[i:j+1]) and len(list(dict.fromkeys(word[i:j+1])))==5:
                        ans=ans+1
                        #print(ans,word[i:j+1])
        
        return ans
