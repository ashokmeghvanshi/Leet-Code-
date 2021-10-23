class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        
        k=0
        
        s=word
        ans=0
        while k<len(sequence):
            if s in sequence:
                ans=ans+1
            s=s+word
            k=k+1
        
        return ans
