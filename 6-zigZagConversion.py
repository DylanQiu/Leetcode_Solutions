class Solution(object):
    def convert(self, s, numRows):
        """

        :param s: str
        :param numRows: int
        :return: str
        """
        if numRows == 1 or numRows >= len(s):
            return s
        layer = [''] * numRows
        i, direct = 0, 0 # direct 0 go down, 1 go up

        for x in s:
            layer[i] += x
            if direct == 0:
                i += 1
            if direct == 1:
                i -= 1
            if i == numRows-1:
                direct = 1
            if i == 0:
                direct = 0
        return ''.join(layer)

a = Solution()
print a.convert("AB", 1)