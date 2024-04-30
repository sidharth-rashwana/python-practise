
def breakingRecords(scores):
    low_score = 0
    low_count = 0
    high_score = 0
    high_count = 0
    for index, score in enumerate(scores):
        if index == 0:
            low_score = high_score = score
        elif score < low_score:
            low_score = score
            low_count += 1
        elif score > high_score:
            high_score = score
            high_count += 1
    return [high_count, low_count]


print(breakingRecords([10, 24, 10, 24]))
