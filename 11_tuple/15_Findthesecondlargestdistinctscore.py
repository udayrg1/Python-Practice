'''
Challenge 7 — Find the second-largest distinct score

Given: scores = (85, 92, 67, 78, 95, 92, 85)

Expected output: 92

Rules:
- Don't use sorted() or max().
- The second-largest value must be distinct.
- Build the logic using loops and conditions.
Hint: The largest value is 95. You now need to identify the largest value that is smaller than 95.

Your turn, ra! Let's see that independent logic-building in action. 😎🔥
'''

scores = (85, 92, 67, 78, 95, 92, 85)

largest_score = scores[0]
second_largest_score = None

for score in scores:
    if score > largest_score:
        second_largest_score = largest_score
        largest_score = score

    elif score < largest_score and (second_largest_score is None or score > second_largest_score):
        second_largest_score = score

print(second_largest_score)