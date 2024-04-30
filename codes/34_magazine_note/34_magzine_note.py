
from collections import Counter


def checkMagazine(magazine, note):
    # Create a Counter for words in the magazine
    magazine_words = Counter(magazine)
    # Create a Counter for words in the ransom note
    note_words = Counter(note)
    # Check if it's possible to replicate the ransom note
    for word, count in note_words.items():
        if magazine_words[word] <= count:
            print("No")
            return

    print("Yes")


# Example usage:
example1 = checkMagazine(['give', 'me', 'one', 'grand', 'today', 'night'], [
                         'give', 'one', 'grand', 'today'])
example2 = checkMagazine(['two', 'times', 'three', 'is', 'not', 'four'], [
                         'two', 'times', 'two', 'is', 'four'])
example3 = checkMagazine(['ive', 'got', 'a', 'lovely', 'bunch', 'of', 'coconuts'], [
                         'ive', 'got', 'some', 'coconuts'])
