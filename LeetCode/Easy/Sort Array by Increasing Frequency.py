class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        
        d={}
        for i in nums:
            if i not in d:
                d[i]=1
            else:
                d[i]=d[i]+1
        print(d)
        d=sorted(d.items(), key=lambda x: x[1])
        print(d)
        res=[]
        i=0
        while i<len(d):
            a,b=d[i][0],d[i][1]
            j=i
            mid=[]
            while j<len(d):
                if d[j][1]==b:
                    mid.append(d[j][0])
                j=j+1
            mid=sorted(mid)[::-1]
            for k in mid:
                res=res+[k]*b
            print(mid,res,j)
            
            if len(mid)==1:
                i=i+1
            else:
                i=i+len(mid)
            
        return res
    
    
