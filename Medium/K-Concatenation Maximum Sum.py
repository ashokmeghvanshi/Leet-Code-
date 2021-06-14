class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        
        def maxSubArraySum(a): 

            max_so_far =a[0] 
            curr_max = a[0] 

            for i in range(1,len(a)): 
                curr_max = max(a[i], curr_max + a[i]) 
                max_so_far = max(max_so_far,curr_max) 
            
            if max_so_far<0:
                return 0
            else:
                return max_so_far
        
        if(k == 1):
            return maxSubArraySum(arr) % (10**9+7)
        
        sumOfarr = sum(arr)
        sumOfconcat = maxSubArraySum(arr*2) % (10**9+7)
        
        if(sumOfarr>0):
            return (sumOfconcat + (sumOfarr*(k-2)))%(10**9+7)
        else:
            return sumOfconcat
        
