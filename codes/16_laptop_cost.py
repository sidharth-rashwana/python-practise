def maxCost(cost, labels, dailyCount):
    ans = 0
    cur_cnt = 0
    cur_cost = 0
    for c, l in zip(cost, labels):
        cur_cost += c
        if l == "illegal":
            continue
        cur_cnt += 1
        if cur_cnt == dailyCount:
            ans = max(ans, cur_cost)
            cur_cnt = 0
            cur_cost = 0
    return ans


# Sample cost data
cost = [10, 15, 5, 12, 20, 8, 17, 6, 11, 14]

# Sample label data
labels = [
    "legal",
    "legal",
    "illegal",
    "legal",
    "legal",
    "illegal",
    "legal",
    "legal",
    "legal",
    "illegal"]

# Sample dailyCount
dailyCount = 3

# Call the function with the sample data
result = maxCost(cost, labels, dailyCount)

# Display the result
print("Maximum cost considering a daily count of", dailyCount, "is:", result)
