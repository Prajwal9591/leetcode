class Solution(object):
    def isValid(self, s):
        stack = []
        for i in range(len(s)):
            c = s[i]
            if (c=='('):
                stack.append(")")
            elif (c=='['):
                stack.append("]")
            elif (c=='{'):
                stack.append("}")
            elif not  stack or stack.pop()!=c :
                return False
        return len(stack)==0  
        """
        :type s: str
        :rtype: bool
        """
        