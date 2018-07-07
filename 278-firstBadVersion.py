# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
def isBadVersion(version):
    return version

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l, r = 0, n
        while l<r:
            if isBadVersion((l+r)/2) and not isBadVersion((l+r)/2-1):
                return (l+r)/2
            elif isBadVersion((l+r)/2):
                r = (l+r)/2
            else:
                l = (l+r)/2