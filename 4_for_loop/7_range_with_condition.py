"""
⭐ Question 7: range() with a condition
Given this list:
prices = [250, 450, 600, 800, 1000]



Use a for loop with range() to print only the prices greater than 500, using their list indexes.
Expected output:
600
800
1000


Hint: You can access a list element using prices[index].
"""

prices = [250, 450, 600, 800, 1000]

for index in range(len(prices)):
    if prices[index] > 500:
        print(prices[index])