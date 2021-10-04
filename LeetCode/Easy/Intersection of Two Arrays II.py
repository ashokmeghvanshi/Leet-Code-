class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        ans=[]
        check=[]
        for i in nums1:
            if i in nums2 and i not in check:
                c1=nums1.count(i)
                c2=nums2.count(i)
                if c1<c2:
                    ans=ans+[i]*c1
                elif c1>c2:
                    ans=ans+[i]*c2
                if c1==c2:
                    ans=ans+[i]*c1
                
            check.append(i)
        
        return ans
