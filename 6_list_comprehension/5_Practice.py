prices = [1000, 500, 2500, 700, 4000]

#You want only prices greater than ₹1000.

expensive_prices = [price for price in prices if price > 1000]

print(expensive_prices)