class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        shortest = min(strs, key=len)
        for i, ch in enumerate(shortest):
            for other in strs:
                if other[i] != ch:
                    return shortest[:i]
        return shortest

# class Solution:
#     # @return a string
#     def longestCommonPrefix(self, strs):
#         if not strs:
#             return ""
#
#         for i, letter_group in enumerate(zip(*strs)):
#             if len(set(letter_group)) > 1:
#                 return strs[0][:i]
#         else:
#             return min(strs)

# class Solution:
#     def lcp(self, str1, str2):
#         i = 0
#         while (i < len(str1) and i < len(str2)):
#             if str1[i] == str2[i]:
#                 i = i+1
#             else:
#                 break
#         return str1[:i]
#
#     # @return a string
#     def longestCommonPrefix(self, strs):
#         if not strs:
#             return ''
#         else:
#             return reduce(self.lcp,strs)
