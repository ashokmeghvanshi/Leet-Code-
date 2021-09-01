class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], num_wanted: int, use_limit: int) -> int:
        
        
        d={}
        for i in range(len(labels)):
            if labels[i] not in d:
                d[labels[i]]=[values[i]]
            else:
                d[labels[i]].append(values[i])
                d[labels[i]]=sorted(d[labels[i]])
        result=[]
        for i in d:
            #print(sorted(d[i])[::-1][:use_limit])
            result=result+d[i][::-1][:use_limit]
            
        #print(d,result)
        result=sorted(result)[::-1][:num_wanted]
        return sum(result)
