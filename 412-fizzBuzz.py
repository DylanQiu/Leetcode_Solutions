class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        l = []
        for i in range(1, n+1):
            if i % 15 == 0:
                l.append("FizzBuzz")
                continue
            if i % 5 == 0:
                l.append("Buzz")
                continue
            if i % 3 == 0:
                l.append("Fizz")
                continue
            l.append(str(i))
        return l