class Solution(object):
    def moveZeroes(self, nums):
        left,right=0,len(nums)-1
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[left],nums[i]=nums[i],nums[left]
                left+=1
        return nums
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        