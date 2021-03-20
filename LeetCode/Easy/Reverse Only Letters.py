class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        S=list(S)
        
        i,j=0,len(S)-1
        
        while i<len(S) and j>-1:
            if i>=j:
                break
            if S[i].isalpha()==True and S[j].isalpha()==True:
                S[i],S[j]=S[j],S[i]
                i=i+1
                j=j-1
            elif S[i].isalpha()==True and S[j].isalpha()==False:
                j=j-1
            elif S[i].isalpha()==False and S[j].isalpha()==True:
                i=i+1
            elif S[i].isalpha()==False and S[j].isalpha()==False:
                i=i+1
                j=j-1
        return ''.join(S)
            
            
                
