class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles=sorted(piles)
        step=len(piles)//3

        result=0
        for i in range(1,step+1):
            result=result+piles[len(piles)-2*i]
        
        return result
