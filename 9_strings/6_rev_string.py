#Reverse a string

order_id = "ORD12345"

#method_1
print(order_id[::-1])

#method_2
order_id = "ORD12345"
rev_id = ""

for char in order_id:
    rev_id = char + rev_id
print(rev_id)

#method_3
order_id = "ORD12345"
rev_id = ""
index = len(order_id)-1

while index >= 0:
    rev_id += order_id[index]
    index -= 1
print(rev_id)