class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        result=[]
        for i,j in zip(l,r):
            arr=sorted(nums[i:j+1])
            if len(arr)<2:
                result.append(True)
            else:
                s=1
                t=arr[1]-arr[0]
                for k in range(len(arr)-1):
                    if arr[k+1]-arr[k]==t:
                        s=s+1
                if s==len(arr):
                    result.append(True)
                else:
                    result.append(False)
        return result
