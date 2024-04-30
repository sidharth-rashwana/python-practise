def flippingBits(n):
    return n ^ 0xFFFFFFFF


result = flippingBits(2147483647)
print(result)
# here output is coming wrong but it should be : 4294967294
