def solution(A, K, L):
    n = len(A)

    if K + L > n:
        return -1

    max_sum_alice = -1

    for i in range(n - K + 1):
        sum_alice = sum(A[i:i + K])
        if sum_alice > max_sum_alice:
            max_sum_alice = sum_alice

    max_sum_bob = -1

    for i in range(n - L + 1):
        sum_bob = sum(A[i:i + L])
        if sum_bob > max_sum_bob:
            max_sum_bob = sum_bob

    if max_sum_alice == -1 or max_sum_bob == -1:
        return -1  # No valid split found for Alice or Bob

    return max_sum_alice + max_sum_bob


print(solution([6, 1, 4, 6, 3, 2, 7, 4], 3, 2))
