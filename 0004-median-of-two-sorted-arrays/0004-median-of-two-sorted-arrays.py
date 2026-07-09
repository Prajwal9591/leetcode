class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        # Always binary search on the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        low, high = 0, m

        while low <= high:
            partitionX = (low + high) // 2
            partitionY = (m + n + 1) // 2 - partitionX

            # Handle edge cases
            leftX = float('-inf') if partitionX == 0 else nums1[partitionX - 1]
            rightX = float('inf') if partitionX == m else nums1[partitionX]

            leftY = float('-inf') if partitionY == 0 else nums2[partitionY - 1]
            rightY = float('inf') if partitionY == n else nums2[partitionY]

            # Correct partition found
            if leftX <= rightY and leftY <= rightX:
                if (m + n) % 2 == 0:
                    return (max(leftX, leftY) + min(rightX, rightY)) / 2.0
                else:
                    return float(max(leftX, leftY))

            # Move towards the correct partition
            elif leftX > rightY:
                high = partitionX - 1
            else:
                low = partitionX + 1