# pangram : if all letters exist in a string
import string


def pangrams(s):
    alphabet = set(string.ascii_lowercase)
    input_string = s.lower()
    if alphabet <= set(input_string):
        return 'pangram'
    return 'not pangram'


s1 = 'We promptly judged antique ivory buckles for the next prize'
print(pangrams(s1))

s2 = 'We promptly judged antique ivory buckles for the prize'
print(pangrams(s2))

s3 = 'abcdefghijkl mnopqrstuvwxyz'
print(pangrams(s3))
