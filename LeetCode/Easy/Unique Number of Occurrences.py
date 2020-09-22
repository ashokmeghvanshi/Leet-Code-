class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        if len(arr)==1 or len(arr)==0:
            return True
        u=list(dict.fromkeys(arr))
        d=[]
        for i in u:
            if arr.count(i) not in d:
                d.append(arr.count(i))
            else:
                return False
        return True
