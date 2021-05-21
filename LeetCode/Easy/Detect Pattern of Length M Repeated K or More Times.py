class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        
        i=0
        ans=0
        while i<len(arr):
            p=arr[i:i+m]
            j=i+m
            s=1
            #print('p',i,i+m,p)
            t=i+m
            while j<len(arr):
                if p==arr[j:j+m] and j==t:
                    s=s+1
                    t=t+1
                    #print('m',i,j,j+m,arr[j:j+m])
                j=j+1
            if s>=k:
                ans=1
            #print(s,ans)
            i=i+1
        if ans==0:
            return False
        else:
            return True
