class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        
        result=[first]
        
        for i in range(len(encoded)):
            a=bin(encoded[i])[2:]
            b=bin(result[i])[2:]
            a=int(a,2)
            b=int(b,2)
            result.append(a^b)
        return result
