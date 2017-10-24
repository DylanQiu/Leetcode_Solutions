class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        cur_sum = 0
        cur_list = []

        if not ops:
            return 0
        for score in ops:
            if score == 'D':
                tmp = cur_list[-1]*2
                cur_sum += tmp
                cur_list.append(tmp)
            elif score == 'C':
                tmp = cur_list.pop()
                cur_sum -= tmp
            elif score == '+':
                tmp = cur_list[-1] + cur_list[-2]
                cur_sum += tmp
                cur_list.append(tmp)
            else:
                cur_sum += int(score)
                cur_list.append(int(score))
        return cur_sum
