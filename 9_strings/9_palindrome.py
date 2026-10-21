word = "MADAM"

rev_word = ""

for char in word:
    rev_word = char + rev_word

if word == rev_word:
    print("Palindrome")
else:
    print("Not a Palindrome")