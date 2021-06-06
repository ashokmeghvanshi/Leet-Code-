class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        ans=''
        i=0
        j=0
        while i<len(word1) and j<len(word2):
            ans=ans+word1[i]+word2[j]
            i=i+1
            j=j+1
        ans=ans+word1[i:]+word2[j:]
        
        return ans
