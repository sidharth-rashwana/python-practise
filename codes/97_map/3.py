# Define a function to square a number
def square(x):
    return x ** 2


# Create a list of numbers
numbers = [1, 2, 3, 4, 5]

# Use map() to apply the square function to each element in the list
squared_numbers = map(square, numbers)

# Convert the result to a list (as map() returns an iterable)
result_list = list(squared_numbers)

# Output the squared numbers
print(result_list)
