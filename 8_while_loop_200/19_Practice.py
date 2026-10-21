'''
🐍⚔️ Q19/200 — Count a Specific Digit

Now let's change the pattern again.

🎯 Task

Write a Python program that:

Uses a while loop
Takes a positive integer
Takes another digit from the user
Counts how many times that digit appears in the number
Prints the count
Do not convert the number to a string
Do not use count()
Do not use a for loop
Example
Enter a number: 1223332
Enter digit to search: 2

Digit 2 appears 3 times.

Because:

1223332
 ↑ ↑   ↑
 2 2   2

Another:

Enter a number: 55512355
Enter digit to search: 5

Digit 5 appears 5 times.
'''

number = int(input("Enter a number: ")) 

search_digit = int(input("Enter a search digit: "))

count = 0

while number > 0:

    digit = number % 10

    if digit == search_digit:
        count += 1

    number = number // 10

print(count)