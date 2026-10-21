#Find the average price without using any statistics libraries.

#method1

prices = (100, 250, 75, 500, 125)

average = ((sum(prices)/len(prices)))

print(average)

#method 2

prices = (100, 250, 75, 500, 125)

sum_of_prices = 0
count_of_prices = 0

for price in prices:
    sum_of_prices += price
    count_of_prices += 1

if count_of_prices > 0:
    average_of_prices = sum_of_prices / count_of_prices
    print(average_of_prices)
else:
    print("count_of_prices value should be greater than zero")