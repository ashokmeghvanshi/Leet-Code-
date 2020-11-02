class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        t=[]
        i=0
        while 2*i+1<len(nums):
            a,b=nums[2*i],nums[2*i+1]
            c=[b]*a
            t=t+c
            #print(t,i)
            i=i+1
        return t
