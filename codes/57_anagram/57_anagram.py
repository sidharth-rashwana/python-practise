"When every letter of target is present in string"


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sorted_target = [''.join(sorted(t))]
        sorted_string = [''.join(sorted(s))]
        if sorted_target == sorted_string:
            return True
        return False


s1 = Solution()
print(s1.isAnagram(s="anagram", t="nagaram"))
