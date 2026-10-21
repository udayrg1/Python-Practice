"""
Question 3: Sort Product Prices
Problem

Create this list of product prices:

prices = [999, 499, 1299, 299, 799]

Perform these tasks:

Print the original list.
Sort the prices in ascending and descending order using .sort().
Print the sorted list.
Print the total number of prices using len().
Expected Output
Original Prices: [999, 499, 1299, 299, 799]
Sorted Prices: [299, 499, 799, 999, 1299]
Total Prices: 5
"""

#length = len(prices)


#solution
prices = [999, 499, 1299, 299, 799]

print(f"Original Prices: {prices}")


#Asc Order
prices.sort()
print(f"Ascending order sorted Prices: {prices}")

#Desc Order
prices.sort(reverse=True)
print(f"Descending order sorted Prices: {prices}")

print(f"Total Prices: {len(prices)}")