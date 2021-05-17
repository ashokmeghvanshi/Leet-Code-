class Solution:
    def findLucky(self, arr: List[int]) -> int:
        
        result=[]
        
        for i in arr:
            if i not in result and arr.count(i)==i:
                result.append(arr.count(i))
        
        if len(result)==0:
            return -1
        elif len(result)==1:
            return result[0]
        if len(result)>1:
            result=sorted(result)
            return result[-1]
        
