class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        if len(nums)<3:
            return False
        stack=[]
        arr=[nums[0]]
        for i in range(1,len(nums)):
            arr.append(min(arr[i-1],nums[i]))
        
        for j in range(len(nums)-1,-1,-1):
            if nums[j]>arr[j]:
                while len(stack)>0 and stack[-1]<=arr[j]:
                    stack.pop()
                if len(stack)>0 and stack[-1]<nums[j]:
                    return True
                stack.append(nums[j])
        return False
            
