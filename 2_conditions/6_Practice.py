#Print before checking

products = [
    "Samsung",
    "OnePlus",
    "iPhone",
    "Vivo",
    "Oppo"
]

for product in products:
    print(product)

    if product == "iPhone":
        print("Found iPhone")
        break


#Print after checking

products = [
    "Samsung",
    "OnePlus",
    "iPhone",
    "Vivo",
    "Oppo"
]

for product in products:
    if product == "iPhone":
        print("Found iPhone")
        break

    print(product)