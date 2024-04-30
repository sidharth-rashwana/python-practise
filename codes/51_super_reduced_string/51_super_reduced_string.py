def superReducedString(s):
    stack = []
    for char in s:
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)
    if len(stack) != 0:
        s = ''.join(stack)
        return s
    else:
        return 'Empty String'


print(superReducedString('aaabccddd'))
