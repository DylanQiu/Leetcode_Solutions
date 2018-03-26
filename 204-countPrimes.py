class Solution(object):
    # def isPrime(self, n):
    #     return all(n % i for i in xrange(2, n / 2 + 1))

    # def countPrimes(self, n):
    #     """
    #     count the number of prime numbers less than a non-negative number, n.
    #     :param n:
    #     :return:
    #     """
    #     count = 0
    #     for i in xrange(1, n):
    #         if self.isPrime(i):
    #             count += 1
    #     return count
    def countPrimes(self, n):
        if n < 3:
            return 0
        primes = [True]*n
        primes[:2] = [False, False]
        for base in xrange(2, int((n)**0.5)+1):
            if primes[base]:
                primes[base**2::base] = [False]*len(primes[base**2::base])
        return sum(primes)


a = Solution()
print a.countPrimes(10000000)

