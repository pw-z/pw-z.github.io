# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:

    @staticmethod
    def isBadVersion(x):
        pass
    
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        利用二分查找，如果是good，则目标在右侧，如果是bad，则目标命中或者在左侧
        """
        l,r = 1,n
        target = n+1
        while l<=r:
            m = (r-l)//2 + l
            if Solution.isBadVersion(m):
                if  m < target:
                    target = m
                r = m-1
            else:
                l = m+1
        return target
                
    
    