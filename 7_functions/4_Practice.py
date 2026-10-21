'''
🎯 Function Practice #3 — Multiple Return Values

This one introduces a new logic pattern, not just another calculation.

Problem

Create a function called:

analyze_product(price, quantity)

The function should:

Calculate the total cost → price × quantity
Calculate the average cost per item → total cost ÷ quantity
Return both values
Don't use print() inside the function

Then call the function for:

price = 500
quantity = 4

Expected values:

Total cost: 2000
Average cost: 500
'''

def analyze_product(price, quantity):
    total_cost = price * quantity
    avg_cost_per_item = total_cost / quantity

    return total_cost, avg_cost_per_item

result = analyze_product(500, 4)
print(result)

'''
def analyze_product(price, quantity):
    total_cost = price * quantity
    avg_cost_per_item = total_cost / quantity

    return total_cost, avg_cost_per_item


total_cost, avg_cost_per_item = analyze_product(500, 4)

print("Total cost:", total_cost)
print("Average cost:", avg_cost_per_item)
'''