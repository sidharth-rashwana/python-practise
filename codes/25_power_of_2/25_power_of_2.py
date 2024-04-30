"""
You can determine if a number is a power of 2 by checking if it has exactly one bit set to 1 in its binary
representation. In other words, a number is a power of 2 if and only if it is in the form of 2^k,
where k is a non-negative integer.
"""


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        # if a given integer n is a power of 2 or not.
        return (n & (n - 1)) == 0


s1 = Solution()
print(s1.isPowerOfTwo(2))
