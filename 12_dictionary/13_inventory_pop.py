'''
4. Your first practice problem
Let's start with a simple problem before moving to the HR scenario.

Imagine you're managing a company's inventory.
inventory = {    "laptop": 10,    "keyboard": 25,    "mouse": 40,    "monitor": 15}


Requirements
1. Remove "keyboard" using pop() and store its returned value in a variable.
2. Print the removed value.
3. Print the updated dictionary.
4. Try removing "printer" using pop() with a default value of "Product Not Found".
5. Print the result.
6. Print the dictionary again to verify whether "printer" was added.
Expected output:
25
{'laptop': 10, 'mouse': 40, 'monitor': 15}
Product Not Found
{'laptop': 10, 'mouse': 40, 'monitor': 15}

'''

inventory = {    
    "laptop": 10,    
    "keyboard": 25,    
    "mouse": 40,    
    "monitor": 15
    }

removed_pair = inventory.pop("keyboard")
print(removed_pair)

print(inventory)

removed_item = inventory.pop("printer", "Product Not Found")
print(removed_item)

print(inventory)