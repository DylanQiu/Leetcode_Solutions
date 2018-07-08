class Solution(object):
    def reverseVowels(self,s):
        """
        :param s: str
        :return: str
        """
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        if not s:
            return ''
        i, j = 0, len(s)-1
        s = list(s)
        while i < j:
            if s[i] not in vowels:
                i += 1
            if s[j] not in vowels:
                j -= 1
            if s[i] in vowels and s[j] in vowels:
                print s[i], s[j]
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1
        return ''.join(s)

a = Solution()
print a.reverseVowels("race a car")