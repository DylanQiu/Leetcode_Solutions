class Solution(object):
    # def letterCombinations(self, digits):
    #     """
    #     :type digits: str
    #     :rtype: List[str]
    #     """
    #     if '' == digits:
    #         return []
    #     kvmaps = {
    #         '2':'abc',
    #         '3':'def',
    #         '4':'ghi',
    #         '5':'jkl',
    #         '6':'mno',
    #         '7':'pqrs',
    #         '8':'tuv',
    #         '9':'wxyz'
    #     }
    #
    #     return reduce(lambda acc, digit: [x+y for x in acc for y in kvmaps[digit]], digits, [''])
    #

    def letterCombinations(self, digits):
        maps = ['0', '1', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        ans = []
        if len(digits) == 0:
            return ans
        for i in xrange(len(digits)):
            x = ord(digits[i])-ord('0')
            if i == 0:
                for s in maps[x]:
                    ans.append(s)
            while len(ans[0]) == i:
                t = ans.pop(0)
                for s in maps[x]:
                    ans.append(t+s)
        return ans


a = Solution()
print a.letterCombinations("23")