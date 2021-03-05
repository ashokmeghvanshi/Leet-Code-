class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        ans=0
        boxTypes.sort(key = lambda x: x[1]) 
        
        for j in boxTypes[::-1]:
            
            if truckSize<1:
                break
            if truckSize>=j[0]:
                ans=ans+j[0]*j[1]
            else:
                ans=ans+truckSize*j[1]
                    
            truckSize=truckSize-j[0]
        
        return ans
    
