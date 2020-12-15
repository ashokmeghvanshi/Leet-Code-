class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        
        p=[x for x in range(1,m+1)]
        result=[]
        for i in range(len(queries)):
            result.append(p.index(queries[i]))
            p.remove(queries[i])
            p.insert(0,queries[i])
        return result
