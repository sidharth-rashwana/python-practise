def check_prime(n):
    if n <= 1:
        return False
    for i in range(3, int(n)):
        if n % i == 0:
            return False
    return True


def count_prime_triplets(arr):
    count = 0
    N = len(arr)

    for i in range(N):
        for j in range(i + 1, N):
            for k in range(j + 1, N):
                if i < j < k:
                    product = arr[i] * arr[j] * arr[k]
                    if check_prime(product):
                        count += 1
    return count


# Input format
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(arr)
    """
    2

    4
    4 5 6 2

    4
    1 1 4 5
    """
    result = count_prime_triplets(arr)
    print(result)
