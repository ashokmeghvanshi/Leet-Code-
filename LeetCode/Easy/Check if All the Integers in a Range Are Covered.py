class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        
        ans=0
        check=0
        for i in range(left,right+1):
            for j in ranges:
                #print(j,i,ans)
                if i in range(j[0],j[1]+1):
                    ans=ans+1
                    check=1
                    break
        #print(ans,check)
        if ans ==right-left+1 and check==1:
            return True
        return False
