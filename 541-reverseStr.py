class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        slist = list(s)
        for i in range(0, len(s), 2*k):
            slist[i:i+k] = reversed(slist[i:i+k])
            l, r = i, min(i+k-1, len(s)-1)
            while l < r:
                slist[l], slist[r] = slist[r], slist[l]
                l+=1
                r-=1
        return "".join(slist)