# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        s,e=1,n
        minvalue=0
        
        while s<=e:
            m=(s+e)//2
            if isBadVersion(m)==True:
                e=m-1
                minvalue=m
            else:
                s=m+1
                
        return minvalue
