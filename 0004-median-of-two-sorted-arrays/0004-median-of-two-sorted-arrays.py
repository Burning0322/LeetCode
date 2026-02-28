class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        merge = nums1 + nums2
        merge.sort()
        m_len = len(merge)

        if m_len%2 == 1:
            return float(merge[m_len//2])
        else:
            mid1 = merge[m_len//2-1]
            mid2 = merge[m_len//2]
            return ((mid1+mid2)/2.0)