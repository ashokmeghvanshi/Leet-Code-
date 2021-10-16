class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        
        text=text.split()
        #print(text)
        ans=len(text)
        
        for i in text:
            for j in brokenLetters:
                if j in i:
                    ans=ans-1
                    break
        
        return ans
        
