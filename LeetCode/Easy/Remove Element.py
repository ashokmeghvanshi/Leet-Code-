class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        length=len(nums)
        
        i=0
        while i<length:
            
            if nums[i]==val:
                nums[i]=nums[length-1]
                length=length-1
            else:
                i=i+1
        
        return length
