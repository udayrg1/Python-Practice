"""
Question 5: Unique Brand Names (Set)
Interview Definition

A Set is an unordered collection of unique items. It does not allow duplicate values.

Problem

Create a set containing the following brands:

Apple
Samsung
OnePlus
Apple
Vivo
Samsung

Perform the following tasks:

Create the set.
Print the complete set.
Add "Google" using .add().
Print the updated set.
Remove "Vivo" using .remove().
Print the final set.
Print the total number of unique brands using len().

Expected Output

Note: Sets are unordered, so your output order may differ.

Brands: {'Apple', 'Samsung', 'OnePlus', 'Vivo'}

Updated Brands: {'Apple', 'Samsung', 'OnePlus', 'Vivo', 'Google'}

Final Brands: {'Apple', 'Samsung', 'OnePlus', 'Google'}

Total Brands: 4
"""

brands = {"Apple","Samsung","OnePlus","Apple","Vivo","Samsung"}

print(f"Brands: {brands}")

brands.add("Google")

print(f"Updated Brands: {brands}")

brands.remove("Vivo")

print(f"Final Brands: {brands}")

total_brands = len(brands)

print(f"Total Brands: {total_brands}")




