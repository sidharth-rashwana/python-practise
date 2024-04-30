def solution(A, K, L):
    n = len(A)

    if K + L > n:
        return -1

    max_sum_alice = -1
    alice_pair = []

    for i in range(n - K + 1):
        sum_alice = sum(A[i:i + K])
        if sum_alice > max_sum_alice:
            max_sum_alice = sum_alice
            alice_pair = A[i:i + K]

    # Remove Alice's elements from the array
    for element in alice_pair:
        A.remove(element)

    max_sum_bob = -1
    bob_pair = []

    for i in range(len(A) - L + 1):
        sum_bob = sum(A[i:i + L])
        if sum_bob > max_sum_bob:
            max_sum_bob = sum_bob
            bob_pair = A[i:i + L]

    if not alice_pair or not bob_pair:
        return -1  # No valid split found for Alice or Bob

    return alice_pair, bob_pair


print(solution([6, 1, 4, 6, 3, 2, 7, 4], 3, 2))
