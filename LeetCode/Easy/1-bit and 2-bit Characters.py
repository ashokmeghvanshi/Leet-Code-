class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        
        two=[11,10]
        i=0
        while i<len(bits)-1:
            
            s=int(str(bits[i])+str(bits[i+1]))
            if s in two:
                i=i+2
            else:
                i=i+1
        if i==len(bits)-1:
            return True
        return False
        
