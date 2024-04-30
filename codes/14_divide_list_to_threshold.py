def divide_list_to_threshold(lst, divisor, threshold):
    count = 0

    while not all(x == lst[0] for x in lst) or len(lst) < threshold:
        lst = [int(x / divisor) for x in lst]
        count += 1

    return count


# Test the function with the provided list and divisor
given_list = [64, 30, 32, 34, 33]
divisor = 2
threshold = 3
result = divide_list_to_threshold(given_list, divisor, threshold)
print(
    "List can be divided",
    result,
    "times to get",
    threshold,
    "equal elements.")
