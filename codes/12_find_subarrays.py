def subarrays(arr):
    final = []
    sub_array = []
    for i in arr:
        if i not in sub_array:
            sub_array.append(i)
            count = arr.count(i)
            final.append([i] * count)
    return final


print(subarrays([1, 1, 2, 2, 3, 3, 3]))
