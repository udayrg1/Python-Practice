'''
Your first practice task
Imagine you're scraping product information from a competitor website.
Requirements:
- Store the product name in product_name.
- Store the brand in brand.
- Store the price in price.
- Print the result in this format: Samsung Monitor costs ₹12500
- Print it once using concatenation (+) and once using an f-string.
Use these values: Samsung, Monitor, and 12500.

'''

product_name = "black LED monitor"
brand = "Samsung"
price = 12500

print(f"{brand} {product_name} costs ₹{price}")

print(brand+" "+product_name+" "+"costs ₹"+str(price))