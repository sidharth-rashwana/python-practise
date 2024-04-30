"""
A robot moves in a plane starting from the original point (0,0).
The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps.
The trace of robot movement is shown as the following:
UP 5
DOWN 3
LEFT 3
RIGHT 2
¡­
The numbers after the direction are steps.
Please write a program to compute the distance from current position
after a sequence of movement and original point.
If the distance is a float, then just print the nearest integer.
Example:
If the following tuples are given as input to the program:
UP 5
DOWN 3
LEFT 3
RIGHT 2
Then, the output of the program should be:
2
"""


def direction(directions):
    x, y = 0, 0
    for d, v in directions.items():
        if d == "UP":
            y += v
        elif d == "DOWN":
            y -= v
        elif d == "LEFT":
            x -= v
        elif d == "RIGHT":
            x += v
    distance = ((x ** 2) + (y ** 2)) ** 0.5
    return distance


d = {"UP": 5, "DOWN": 3, "LEFT": 3, "RIGHT": 2}
print(direction(d))
