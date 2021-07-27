class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        
        char_even=['a','c','e','g']
        char_odd=['b','d','f','h']
        
        c,n=coordinates[0],int(coordinates[1])
        
        if c in char_even:
            if n%2==0:
                return True
            else:
                return False
        
        
        if c in char_odd:
            if n%2!=0:
                return True
            else:
                return False
        
        
