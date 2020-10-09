class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        s=0
        for i in range(len(arr)):
            for j in range(i,len(arr)):
                if len(arr[i:j+1])%2!=0:
                    #print(arr[i:j+1],sum(arr[i:j+1]))
                    s=s+sum(arr[i:j+1])
        return s
