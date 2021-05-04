class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        
        ans=[]
        i=0
        while i<(len(s)-1):
            t=1
            for j in range(i+1,len(s)):
                if s[i]==s[j]:
                    t=t+1
                    if j==len(s)-1:
                        if t>2:     
                            ans.append([i,j])
                            return ans
                        else:
                            t=1
                            break
                else:
                    if j==len(s)-1 and s[i]==s[j]:
                        if t>2:
                            ans.append([i,j])
                            return ans
                        else:
                            t=1
                            break
                    if t>2:
                        ans.append([i,j-1])
                        i=j-1
                    t=1
                    break
            i=i+1
                
        return ans 
