'''
Day 7 — Next challenge: Vegetable prices 🥦
Create a dictionary named vegetables with these key-value pairs:
Key	Value
"Tomato"	40
"Potato"	30
"Onion"	50
"Carrot"	60

Requirements:
1. Print each vegetable and its price using a loop.
2. Increase the price of "Tomato" to 45.
3. Add "Beans" with a price of 55.
4. Delete "Potato" from the dictionary.
5. Print the final dictionary.
6. Print the total number of remaining vegetables using len().

'''

vegetables = {
    "Tomato" :	40,
    "Potato" :	30,
    "Onion"  :	50,
    "Carrot" :	60
}


for key, value in vegetables.items():
    print(key, ":", value)

vegetables["Tomato"] = 45

vegetables["Beans"] = 55

del vegetables["Potato"]

print(vegetables)

print(len(vegetables))
