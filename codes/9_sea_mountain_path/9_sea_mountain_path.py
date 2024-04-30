def counting_valleys(steps, path):
    altitude = 0
    valleys = 0
    in_valley = False  # Flag to track if currently in a valley

    for step in path:
        if step == 'U':
            altitude += 1
        else:  # 'D' step
            altitude -= 1

        if altitude < 0 and not in_valley:  # Entered a valley
            in_valley = True

        if altitude >= 0 and in_valley:  # Exited a valley
            valleys += 1
            in_valley = False

    return valleys


print(counting_valleys(12, 'DDUUDDUDUUUD'))
