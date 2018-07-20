class Solution(object):
    def compress(self, c):
        flips = [(c[0], 0)] + [(c[i], i) for i in range(1, len(c)) if c[i] != c[i - 1]] + [(None, len(c))]
        chunks = [(b[0], a[1] - b[1]) for (a, b) in zip(flips[1:], flips)]
        compressed = reduce(lambda a, b: (a + [b[0]] + (list(str(b[1])) if (b[1] > 1) else [])), chunks, [])
        c[:len(compressed)] = compressed
        return len(compressed)