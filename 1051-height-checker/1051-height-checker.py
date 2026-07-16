class Solution(object):
    def heightChecker(self, heights):
        list1 = sorted(heights)
        count=0
        for i in range(len(heights)):
            if list1[i]!=heights[i]:
                count +=1
        return count
        """
        :type heights: List[int]
        :rtype: int
        """
        