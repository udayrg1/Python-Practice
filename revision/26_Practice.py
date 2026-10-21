'''
Write a Python program that:

Uses a for loop
Uses range()
Calculates the sum of even numbers from 1 to 20
Prints only the final sum

Expected final result should be a single number.

💡 You can use the same accumulator concept we just learned.
'''

sum_of_even_numbers = 0

for number in range(1,21):
    if number % 2 == 0:
        sum_of_even_numbers = sum_of_even_numbers + number

print(sum_of_even_numbers)