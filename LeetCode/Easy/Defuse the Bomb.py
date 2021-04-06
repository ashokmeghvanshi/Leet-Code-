class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        
        if k==0:
            return [0]*len(code)
        
        result=[]
        if k>0:
            arr=code+code[:k]
            #print(arr)
            for i in range(len(code)):
                result.append(sum(arr[i+1:i+k+1]))
        
        if k<0:
            arr=code[k:]+code
            #print(arr)
            for i in range(len(code)):
                result.append(sum(arr[i:i-k]))

        return result
        
            
