'''
String Practice — Question 2
Scenario: Competitor product scraper
You scraped these details from a competitor website:
product_name = "Wireless Keyboard"brand = "Logitech"price = 2499website = "Amazon"

Your task:
Print the following output using string concatenation (+) only — no f-strings.
Logitech Wireless Keyboard is available on Amazon for ₹2499
'''

product_name = "Wireless Keyboard"
brand = "Logitech"
price = 2499
website = "Amazon"

print(brand+" "+product_name+" "+"is available on"+" "+website+" "+"for ₹"+str(price))