'''
Step 4: Your basic practice problem
Scenario: Online Store Product Catalog
An online store maintains the following product prices:
product_prices = {    "Laptop": 55000,    "Mouse": 800,    "Keyboard": 1500}


The store receives a price update:
- Mouse: ₹750
- Keyboard: ₹1,200
- Monitor: ₹12,000

Your requirements
1. Use update() to apply all three changes.
2. Print the updated dictionary.
3. Print the price of "Mouse".
4. Print the total number of products using len().

Rules:
- Use update() for the changes.
- Don't use if, else, or loops.
- Don't manually change individual dictionary entries.
- Write the complete program yourself.

'''

product_prices = {    
    "Laptop": 55000,    
    "Mouse": 800,    
    "Keyboard": 1500
    }

product_prices.update({
     "Mouse" :  750,
     "Keyboard" : 1200,
     "Monitor" : 12000
})

print(product_prices)

print(product_prices["Mouse"])

print(len(product_prices))