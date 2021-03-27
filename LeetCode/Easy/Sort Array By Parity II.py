class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        
        odd=[]
        even=[]
        for i in A:
            if i%2==0:
                even.append(i)
            else:
                odd.append(i)
        #print(odd,even)
        result=[]
        x,y=0,0
        for i in range(len(A)):
            if i%2==0:
                result.append(even[x])
                x=x+1
            else:
                result.append(odd[y])
                y=y+1
        return result
