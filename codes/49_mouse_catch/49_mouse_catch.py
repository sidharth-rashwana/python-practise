def catAndMouse(x, y, z):
    c1, c2 = 0, 0
    c1 = abs(x - z)
    c2 = abs(y - z)
    if c1 > c2:
        print('Cat B')
    elif c1 < c2:
        print('Cat A')
    else:
        print('Mouse C')
