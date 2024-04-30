class Solution:
    def isPalindrome(self, s: str):
        s = ''.join(c.lower() for c in s if c.isalnum())
        return s == s[::-1]


s1 = Solution()
print(s1.isPalindrome("A man, a plan, a canal: Panama"))
print(s1.isPalindrome("0P"))
