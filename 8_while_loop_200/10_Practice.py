'''
🐍⚔️ Q10/200 — Count Even & Odd Numbers

Write a Python program that:

Uses a while loop
Keeps accepting numbers
Stops when the user enters 0
Counts how many numbers are even
Counts how many numbers are odd
Do not count 0
Prints both final counts
Don't use a list
Must use break

Example:

Enter a number: 10
Enter a number: 7
Enter a number: 22
Enter a number: 15
Enter a number: 8
Enter a number: 0

Even: 3
Odd: 2
'''

even_count = 0
odd_count =  0

while True:
    number = int(input("Enter a number: "))

    if number == 0:
        break

    if number % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
        
print(even_count)
print(odd_count)
    
