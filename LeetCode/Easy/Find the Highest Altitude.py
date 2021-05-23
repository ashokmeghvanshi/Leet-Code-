class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        
        result=[0]
        j=0
        for i in gain:
            result.append(i+result[j])
            j=j+1
        #print(result)
        return max(result)
