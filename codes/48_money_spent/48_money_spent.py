def getMoneySpent(keyboards, drives, b):
    # Initialize the maximum cost to -1, indicating no valid combination found
    # yet.
    max_cost = -1
    for k in keyboards:
        for d in drives:
            total_cost = k + d
            if total_cost <= b and total_cost > max_cost:
                max_cost = total_cost
    return max_cost


keyboards = [3, 1]
drives = [5, 2, 8]
b = 10
print(getMoneySpent(keyboards, drives, b))
