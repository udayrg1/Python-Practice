text = "Education Is mUst"

vowels = "AEIOU"

vowels_separated = ""
reversed_string = ""

for char in text.lower():
    if char in vowels.lower():
        vowels_separated = char + vowels_separated



# Now vowels_separated = "uioiaue"
index = 0 #vowels_separated - index
for letter in text:
     if letter.lower() in  vowels.lower():
        reversed_string += vowels_separated[index]
        index += 1
     else:
        reversed_string += letter

print(reversed_string)


    