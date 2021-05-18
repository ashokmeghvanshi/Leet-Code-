class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        if len(stones)==1:
            return stones[0]
        
        while True:
            
            stones=sorted(stones)
            a,b=min(stones[-1],stones[-2]),max(stones[-1],stones[-2])
            #print(stones,a,b)
            if a==b:
                stones=stones[:-2]
            else:
                stones[-1]=b-a
                #print(stones)
                stones=stones[:-2]+stones[-1:]
            #print(stones)
            if len(stones)<2:
                break
                
        if len(stones)>0:
            return stones[0]
        else:
            return 0
                
                
