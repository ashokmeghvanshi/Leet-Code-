class Solution:
    def numWaterBottles(self, numb: int, nume: int) -> int:
        maxbottle=numb
        empty=numb
        while empty>=nume:
            if empty<nume:
                return maxbottle
            numb=empty//nume
            empty=empty-numb*nume
            maxbottle=maxbottle+numb
            #print(s,numb,emp)
            empty=numb+empty
            
        return maxbottle
