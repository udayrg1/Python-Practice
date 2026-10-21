word = "programming"

seen = ""
unique_word = ""

for char in word:
    if char not in seen:
        unique_word += char
        seen += char
print(unique_word)

