"""
Given a dictionary student_scores, find the student with the highest score and return their name.
"""

student_scores = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "David": 95,
    "Eve": 88
}
highest = sorted(student_scores.items(), key=lambda x: x[1], reverse=True)

print('student with highest marks : ', highest[0][0])
