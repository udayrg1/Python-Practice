number = 1234567890

even_num = ""
rev_num = ""

for num in str(number):
    if int(num) % 2 == 0:
        even_num = num + even_num

index = 0

for digit in str(number):
    if int(digit) in even_num:
        rev_num += even_num[index]
        index += 1
    else:
        rev_num += digit

print(rev_num)