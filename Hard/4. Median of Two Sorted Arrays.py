"""Given two sorted arrays nums1 and nums2 of size m and n respectively, 
return the median of the two sorted arrays.
The overall run time complexity should be O(log (m+n))."""

# Solution:

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # always binary search on smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n   = len(nums1), len(nums2)
        total  = m + n
        half   = total // 2
        lo, hi = 0, m

        while lo <= hi:
            cut1 = (lo + hi) // 2   # partition nums1
            cut2 = half - cut1      # partition nums2

            # boundary values
            L1 = nums1[cut1 - 1] if cut1 > 0 else float('-inf')
            R1 = nums1[cut1]     if cut1 < m else float('inf')
            L2 = nums2[cut2 - 1] if cut2 > 0 else float('-inf')
            R2 = nums2[cut2]     if cut2 < n else float('inf')

            if L1 <= R2 and L2 <= R1:        # valid partition ✅
                if total % 2 == 1:
                    return float(min(R1, R2))
                else:
                    return (max(L1, L2) + min(R1, R2)) / 2.0

            elif L1 > R2:
                hi = cut1 - 1    # move left
            else:
                lo = cut1 + 1    # move right