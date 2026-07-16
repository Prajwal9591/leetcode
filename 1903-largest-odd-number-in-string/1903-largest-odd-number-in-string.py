class Solution(object):
    def largestOddNumber(self, num):
        for i in range(len(num)-1,-1,-1):
            if (ord(num[i])-ord('0'))%2:
                return num[:i+1]
        return ""
        """
        :type num: str
        :rtype: str
        """
        