class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        dic={}
        song_pair=0
        
        for t in time:
            if 60-t%60 in dic:
                song_pair += dic[60-t%60]
            elif t%60==0 and 0 in dic:
                song_pair += dic[0]
            if t%60 not in dic:
                dic[t%60]=0
            dic[t%60]+=1
            
        return song_pair
    
