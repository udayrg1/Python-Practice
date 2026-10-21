#Find the lowest score without using min() or sorted().

scores = (85, 92, 67, 78, 95)

lowest_score = scores[0]

for score in scores:
    if score < lowest_score:
        lowest_score = score
print(lowest_score)