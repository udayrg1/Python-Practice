'''
Create a new list where:

prices = [499, 1200, 2500, 800, 3500]

Keep only prices greater than or equal to 1000
Apply a 10% discount
Store the discounted prices
Expected Output
[1080.0, 2250.0, 3150.0]
'''

prices = [499, 1200, 2500, 800, 3500]

discounted_prices = [price * 0.9 for price in prices if price >= 1000]

print(discounted_prices)