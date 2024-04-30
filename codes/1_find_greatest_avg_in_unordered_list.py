unordered_list = [3, 10, 2, 8, 4, 5]
max_pair = []
max_value = 0
for i in range(len(unordered_list) - 2):
    avg = float(sum(unordered_list[i:i + 3]) / 3)
    if avg > max_value:
        max_pair = unordered_list[i:i + 3]
        max_value = avg
print(max_pair)

print('greatest average of three consecutive', max_pair, ' : ', max_value)