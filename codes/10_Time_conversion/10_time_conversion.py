
def convert(s):
    if s[-2:] == "PM":
        if int(s[:2]) != 12:
            final = int(s[:2]) + 12
            return str(final) + s[2:-2]
        else:
            return s[:-2]
    if s[-2:] == "AM":
        if int(s[:2]) == 12:
            final = int(s[:2]) - 12
            return str(final) * 2 + s[2:-2]
        else:
            return s[:-2]


print(convert("01:10:12PM"))
print(convert("07:05:45PM"))
print(convert("12:05:45AM"))
print(convert("01:05:45AM"))
print(convert("12:00:00AM"))
print(convert("11:00:00PM"))
