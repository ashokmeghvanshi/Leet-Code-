class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        
        ans=0

        # O(N3)
        t=[]
        for a in range(len(nums)):
            for b in range(a+1,len(nums)):
                t.append([nums[a]+nums[b],b])
        #print(t)
        p=[]
        for i in range(len(t)):
            x,y=t[i]
            for j in range(y+1,len(nums)):
                p.append([x+nums[j],j])
        #print(p)
        
        for i in range(len(p)):
            x,y=p[i]
            for j in range(y+1,len(nums)):
                if x==nums[j]:
                    ans=ans+1

        # O(N4) 
        
        # for a in range(len(nums)):
        #     for b in range(a+1,len(nums)):
        #         for c in range(b+1,len(nums)):
        #             for d in range(c+1,len(nums)):
        #                 if nums[a]+nums[b]+nums[c]==nums[d]:
        #                     ans=ans+1
        
        return ans
