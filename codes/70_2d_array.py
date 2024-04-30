"""
Write a program which takes 2 digits, X,Y as
input and generates a 2-dimensional array.
The element value in the i-th row and j-th column of the array should be i*j.
Note: i=0,1.., X-1; j=0,1,¡­Y-1.
Example
Suppose the following inputs are given to the program:
3,5
Then, the output of the program should be:
[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]
"""
x, y = input('Enter x and y (3,4): \n').split(',')

# method-1
overall = []
for i in range(int(x)):
    res = []
    for j in range(int(y)):
        res.append(i * j)
    overall.append(res)
print(overall)

# method-2
arr = [[i * j for j in range(int(y))] for i in range(int(x))]
print(arr)
