class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        c = 0
        for i in range(n):
            m = start + 2*i
            c = c^m
        return c