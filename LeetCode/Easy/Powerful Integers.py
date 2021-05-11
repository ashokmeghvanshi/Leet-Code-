class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        
        result=[]
        i=0
        while x**i<=bound:
            j=0
            while x**i+y**j<=bound:
                
                #print(i,j)
                t=x**i+y**j
                if t<=bound and t not in result:
                    result.append(t)
                if y == 1:
                    break
                
                j=j+1
            if x == 1:
                break
            #print(i)
            i=i+1
            
        #print(result)
        return result
