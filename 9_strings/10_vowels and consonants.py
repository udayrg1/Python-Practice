text = "Automation Testing"

vowels = "AEIOU"

vowles_count = 0
consonants_count = 0


for char in text.lower():
    if char in vowels.lower():
        vowles_count += 1
    elif char.isalpha():
        consonants_count += 1

print(vowles_count)
print(consonants_count)




#Auoaioei

#tmtnTstng