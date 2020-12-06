class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        d={}
        
        for i in range(len(groupSizes)):
            if groupSizes[i] not in d:
                d[groupSizes[i]]=[i]
            else:
                d[groupSizes[i]].append(i)
        result=[]
        for i in d:
            if len(d[i])==groupSizes[d[i][0]]:
                result.append(d[i])
            else:
                t=[]
                for j in d[i]:
                    t.append(j)
                    if len(t)==groupSizes[d[i][0]]:
                        result.append(t)
                        t=[]
                    
        return result 
