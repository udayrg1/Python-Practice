product_code = "RAMAGIRIUDAYKUMAR"
seen = ""
duplicates = ""

for char in product_code:
    if char in seen:
        if char not in duplicates:
            duplicates += char
    else:
        seen += char

print(duplicates)