class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        S = ''.join(S.split('-')).upper()
        length = len(S)
        remainder = K if length % K == 0 else length%K
        cur_idx = remainder
        result = S[:cur_idx]

        while cur_idx < length:
            result += '-' + S[cur_idx:cur_idx+K]
            cur_idx += K
        return result