class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        
        a,l=0,0
        s=0
        while len(piles)>0:
            if s%2==0 and len(piles)==1:
                a=a+piles[0]
                break
            if s%2!=0 and len(piles)==1:
                l=l+piles[0]
                break
                
            if s%2==0:
                if piles[0]>=piles[-1]:
                    a=a+piles[0]
                    piles=piles[1:]
                else:
                    a=a+piles[-1]
                    piles=piles[:-1]
            else:
                if piles[0]<=piles[-1]:
                    l=l+piles[0]
                    piles=piles[1:]
                    
                else:
                    l=l+piles[-1]
                    piles=piles[:-1]
            s=s+1
            
        if a>l:
            return True
        else:
            return False
