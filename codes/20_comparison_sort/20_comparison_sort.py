def countingSort(arr):
    # Create a frequency array with 100 elements initialized to 0
    frequency_array = [0] * 100

    # Count the occurrences of each value in the input array
    for num in arr:
        frequency_array[num] += 1

    return frequency_array


print(countingSort([63, 25, 73, 1, 98]))
