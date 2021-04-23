class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        
        s=''
        for i in licensePlate:
            if i.isalpha()==True:
                s=s+i
        s=s.lower()
        ans=[]
        for i in words:
            t=0
            for j in s:
                
                if j in i and s.count(j)<=i.count(j):
                    t=t+1
            if len(s)==t:
                ans.append(i)
        #print(ans,s)
        ans=sorted(ans, key=len)
        #print(ans)
        return ans[0]
