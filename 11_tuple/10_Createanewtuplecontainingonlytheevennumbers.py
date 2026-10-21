numbers = (12, 7, 4, 9, 16, 3, 8, 11)

even = ()

for num in numbers:
    if num % 2 == 0:
        even += (num,)
print(even)