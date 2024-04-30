
def are_strings_compatible(str1, str2):
    for char1, char2 in zip(str1, str2):
        print(char1, char2)
        diff = ord(char2) - ord(char1)
        if diff < 0:
            return "NO"

        ord_char1 = ord(char1) + diff

        if ord_char1 != ord(char2):
            return "NO"

    return "YES"


# input-1
# abaca
# cdbda
# input-2
# abc
# bcd
# input-3
# abc
# bcd
string1 = input().strip()
string2 = input().strip()
result = are_strings_compatible(string1, string2)
print(result)
