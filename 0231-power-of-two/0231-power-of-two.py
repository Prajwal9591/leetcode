class Solution(object):
    def isPowerOfTwo(self, n):
        if n<=0:
            return False
        else:
            return ((n & (n-1))==0)
            
        """
        :type n: int
        :rtype: bool
        """
        