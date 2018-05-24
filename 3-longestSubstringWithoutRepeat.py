class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """

        :param s: str
        :return: int
        """
        used = dict()
        start = maxlen = 0
        for i in xrange(len(s)):
            if s[i] in used and used[s[i]] >= start:
                start = used[s[i]] + 1
            else:
                maxlen = max(maxlen, i-start+1)
            used[s[i]] = i
        return maxlen
