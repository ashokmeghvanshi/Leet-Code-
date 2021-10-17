class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        
        year={}
        
        for i in logs:
            for j in range(i[0],i[1]):
                if j not in year:
                    year[j]=1
                else:
                    year[j]=year[j]+1
                    
        #print(year)
        year=dict(sorted(year.items(), key=lambda item: item[0]))
        
        #print(year)
        
        year=list(dict(sorted(year.items(),reverse=True, key=lambda item: item[1])).keys())
        
        return year[0]
