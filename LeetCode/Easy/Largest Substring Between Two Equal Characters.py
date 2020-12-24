class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        mx=-1
        
        i=0
        while i<len(s):
            j=i+1
            while j<len(s):
                if s[i]==s[j]:
                    t=j-1-i
                    if t>mx:
                        mx=t
                j=j+1
            i=i+1
        #print(mx)
        return mx
