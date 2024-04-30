class Solution:
    def check_range(self, x):
        min_value = -2**31
        max_value = 2**31 - 1
        if int(x) not in range(min_value, max_value):
            return 0
        return True

    def reverse(self, x: int) -> int:
        sign = str(x)[0::-1]
        if sign == '-':
            reverse = str(x)[:0:-1]
            final = sign + reverse
            if self.check_range(final):
                return int(final)
            return 0
        if self.check_range(str(x)[::-1]):
            return int(str(x)[::-1])
        return 0


s1 = Solution()
print(s1.reverse(9992929292922))
print(s1.reverse(-123))
