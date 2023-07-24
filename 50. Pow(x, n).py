from typing import List

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0: return 1

        if n < 0:
            x = 1 / x
            n = -n

        res = 1
        while n:
            if n & 1:
                res *= x
            x *= x
            n >>= 1

        return res
    