class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        
        deck=sorted(deck)
        result=[0]*len(deck)
        
        queue=[x for x in range(len(deck))]
        #print(queue)
        
        i=0
        while i<len(deck):
            result[queue[0]]=deck[i]
            
            if len(queue)==1:
                result[queue[0]]=deck[i]
                break
            queue=queue[2:]+[queue[1]]
            #print(queue,result)
            i=i+1
        return result
