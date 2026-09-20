class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m = len(nums1)
        n = len(nums2)
        merged_array = [0] * (m + n)
        i = 0
        j = 0
        k = 0

        if m == 0:
            merged_array = nums2
        if n == 0:
            merged_array = nums1

        while i < m and j < n:
            if nums1[i] <= nums2[j]:
                merged_array[k] = nums1[i]
                i += 1
            else:
                merged_array[k] = nums2[j]
                j += 1
            k += 1
        
        while i < m:
            merged_array[k] = nums1[i]
            i += 1
            k += 1
        
        while j < n:
            merged_array[k] = nums2[j]
            j += 1
            k += 1
        
        l = len(merged_array)
        mid = l // 2
        if l % 2 == 1:
            return merged_array[mid]
        else:
            return float(merged_array[mid - 1] + merged_array[mid])/float(2)
