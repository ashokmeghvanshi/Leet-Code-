class Solution:
    def minTimeToType(self, word: str) -> int:
        
        ans=0
        previousword='a'
        
        for currword in word:
            
            previousposition=ord(previousword)
            currposition=ord(currword)
            
            #print('p',previousposition,currposition)
            
            clockwiseSteps = abs(currposition - previousposition)
            antiClockwiseSteps = abs(clockwiseSteps - 26)
            
            #print('c',clockwiseSteps,antiClockwiseSteps)
            
            ans=ans+min(clockwiseSteps,antiClockwiseSteps)
            
            previousword=currword
            
        ans=ans+len(word)
        
        return ans
s
