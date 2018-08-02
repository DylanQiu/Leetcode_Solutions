class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        d = {}
        st = []
        ans = []

        for x in nums:
            while len(st) and st[-1] < x:
                d[st.pop()] = x
            st.append(x)
        for x in findNums:
            ans.append(d.get(x,-1))
        return ans