number = 9876543210

rev_num = ""

for num in str(number):
    rev_num = num + rev_num
print(rev_num)


'''
Why does this work?
- str(number) converts the integer into "9876543210", which you can iterate over.
- num + rev_num adds each digit to the front of the result.
- rev_num must be a string because you're joining characters.
Notice that the output starts with 0. That's because rev_num is a string, so it preserves the leading zero. If you convert the result back to an integer using int(rev_num), the output becomes 123456789.
Nice application of the string-reversal technique you learned earlier, buddy! 💪
'''