product_code = "ABCDFEDCBA"

updated_code = ""

for char in product_code:
    if char in updated_code:
        print(char)
        break
    updated_code += char