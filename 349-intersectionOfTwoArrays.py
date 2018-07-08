class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        col = []
        for i in nums1:
            if i in nums2:
                col.append(i)
        return list(set(col))

a = Solution()
print a.intersection([1,2,3,4], [2,3,4])