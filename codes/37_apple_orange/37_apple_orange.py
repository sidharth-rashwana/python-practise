def countApplesAndOranges(s, t, a, b, apples, oranges):
    total_apples = []
    total_oranges = []

    for apple in range(len(apples)):
        distance = apples[apple] + a
        if s <= distance <= t:
            total_apples.append(distance)

    for orange in range(len(oranges)):
        distance = oranges[orange] + b
        if s <= distance <= t:
            total_oranges.append(orange + b)

    print(len(total_apples))
    print(len(total_oranges))


s = 7
t = 11
apple_tree_loc = 5
orange_tree_loc = 15
apples = [-2, 2, 1]
oranges = [5, -6]
countApplesAndOranges(s, t, apple_tree_loc, orange_tree_loc, apples, oranges)
