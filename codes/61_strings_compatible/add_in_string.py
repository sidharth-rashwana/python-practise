input_string = "yz"


def add_one_to_string(input_string):
    result = ''.join(chr(ord(char) + 1) for char in input_string)
    for char in result:
        if not char.isalpha():
            return 'NO'
    return 'YES'


print(add_one_to_string(input_string))

# check on adding 1 , if they are equal
