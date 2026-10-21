'''
🔥 String Challenge 18 — Mini Project
Amazon product data cleaning time, da! 🛒
product = "  Samsung Galaxy S24 | ₹74999 | In Stock  "



Your task: Clean and extract the product details.
Expected output:
Product: Samsung Galaxy S24
Price: ₹74999
Availability: In Stock
Product Code Position: 8


Rules:
- Use .strip(), .split(), .replace(), and .find().
- Don't use loops or dictionaries.
- Write the code yourself first. No hints unless you ask! 😈
'''

product = "  Samsung Galaxy S24 | ₹74999 | In Stock  "

updated_product = product.replace("|", "$")

split_product = updated_product.split("$")

product_name = split_product[0].strip()
price = split_product[1].strip()
availability = split_product[2].strip()

index = product.find("Galaxy")

print(f"Product: {product_name}")
print(f"Price: {price}")
print(f"Availability: {availability}")
print(f"Product Code Position: {index}")