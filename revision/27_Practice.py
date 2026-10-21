'''
Write a Python program that:

Uses a for loop
Uses range()
Counts how many numbers between 1 and 20 are divisible by 3
Prints only the final count

💡 This time, instead of adding number, you'll increase a counter by 1 whenever the condition is true.
'''

count = 0

for number in range(1,21):
    if number % 3 == 0:
        count = count + 1

print(count)