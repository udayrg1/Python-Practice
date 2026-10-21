'''
String Challenge 14 — Extract Product Information
Imagine you're scraping product data from a website.
product = "Samsung Galaxy S24 | ₹74999 | In Stock"



Your task: Extract and print these three values separately:
Product: Samsung Galaxy S24
Price: ₹74999
Availability: In Stock


Rules:
- Use .split().
- Don't use fixed character indexes or slicing.
- Store the extracted values in separate variables.

'''

product = "Samsung Galaxy S24 | ₹74999 | In Stock"

split_list = product.split("|")

print(split_list)



#split leaves trailing and leading spaces, to overcome this we are using .strip()
product_name = split_list[0].strip()
price = split_list[1].strip()
availability = split_list[2].strip()

print(f"Product: {product_name}")
print(f"Price: {price}")
print(f"Availability: {availability}")