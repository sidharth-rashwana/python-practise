import numpy as np
m = [
    [1, 1, 1],
    [1, 0, 1],
    [0, 1, 1]
]
my_array = np.array(m)

# find index where value is 0
zero_indices = np.argwhere(my_array == 0)

for idx in zero_indices:
    my_array[idx[0], :] = 0  # specific row
    my_array[:, idx[1]] = 0  # specific col

print(my_array)
