class Solution(object):
    def repeatedCharacter(self, s):
        hashmap=set()
        for ch in s:
            if ch in hashmap:
                return ch
            hashmap.add(ch)
        return false
        """
        :type s: str
        :rtype: str
        """
        