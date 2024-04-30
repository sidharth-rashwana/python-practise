import re


def longest_palindrome(s):
    # Function to check if a string is a palindrome
    def is_palindrome(sub):
        return sub == sub[::-1]

    # Find all palindromic substrings in the string
    palindromes = re.findall(r'(?=(\w+))', s)

    # Filter out non-palindromic substrings
    palindromes = [sub for sub in palindromes if is_palindrome(sub)]

    # Find the longest palindrome
    longest_palindrome = max(palindromes, key=len, default="")

    return longest_palindrome


# Example usage
input_string = "babad"
result = longest_palindrome(input_string)
print("Longest Palindrome:", result)
