class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        last_index=0
        till_now=0
        initial=0
        result=[]
        i=0
        while len(s)>i:
            till_now=s.rindex(s[i])
            last_index=max(last_index,till_now)
            if last_index==i:
                result.append(len(s[initial:last_index+1]))
                i=last_index+1
                initial=last_index+1
                last_index=0
            else:
                i+=1
        return result
