"return the index of first non repeating value"


class Solution:
    def firstUniqChar(self, s: str) -> int:
        for index, value in enumerate(s):
            lst = []
            if value not in lst:
                lst.append(value)
                c = s.count(value)
                if c == 1:
                    return index
        return -1


s1 = Solution()
print(s1.firstUniqChar(s="leetcode"))
