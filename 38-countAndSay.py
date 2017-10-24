class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        s = "1"
        for i in range(n-1):
            count = 1
            tmp = []
            for index in range(1, len(s)):
                if s[index] == s[index-1]:
                    count += 1
                else:
                    tmp.append(str(count))
                    tmp.append(s[index-1])
                    count = 1
            tmp.append(str(count))
            tmp.append(s[-1])
            s = ''.join(tmp)
        return s
