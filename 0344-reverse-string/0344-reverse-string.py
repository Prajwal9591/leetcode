class Solution(object):
    def reverseString(self, s):
        left = 0
        right = len(s)-1
        def reverse(left,right):
            if left >= right:
                return
            s[left],s[right] = s[right],s[left]
            return reverse(left+1,right-1)
        return reverse(left,right)
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        