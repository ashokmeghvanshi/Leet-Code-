class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        t=sorted(nums)
        n=len(nums)-1
        for i in range(1,len(nums),2):
            nums[i]= t[n]
            n=n-1
            #print(nums)
        
        for i in range(0,len(nums),2):
            nums[i]=t[n]
            n=n-1
        
