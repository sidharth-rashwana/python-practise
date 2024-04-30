a = [3, 5, 7]
b = [3, 6]
c = [4, 6, 9]


def triplets(a, b, c):
    # Remove duplicates and sort the arrays
    a = sorted(set(a))
    b = sorted(set(b))
    c = sorted(set(c))

    print(a, b, c)

    count = 0  # Initialize count of distinct triplets

    # Iterate through the unique values in array 'b'
    for q in b:
        # Count the number of elements in 'a' less than or equal to 'q'
        count_a = len([p for p in a if p <= q])

        # Count the number of elements in 'c' less than or equal to 'q'
        count_c = len([r for r in c if r <= q])

        # Update the total count of distinct triplets
        count += count_a * count_c

    return count


print(triplets(a, b, c))
