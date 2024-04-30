def prime():
    total_count = int(input('Enter total prime nos required'))
    primes = []
    count = 0
    for i in range(2, 100):
        for j in range(2, i):
            # if divisible by any number other than 2
            if i % j == 0:
                break
        else:
            if count != total_count:
                count += 1
                primes.append(i)
    print(primes)


prime()
