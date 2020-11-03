class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        
        t=[]
        for i in range(len(prices)):
            s=0
            for j in range(i+1,len(prices)):
                if prices[i]>=prices[j]:
                    t.append(prices[i]-prices[j])
                    s=1
                    break
            if s==0:
                t.append(prices[i])
        return t
