'''
Question 3 — Extracting characters
You receive a product code from a competitor website:

product_code = "AMZ-84729-IN"

Your task: Print only the country suffix (IN) by accessing the string using indexing or slicing.
Requirements:
- Don't use .split(), .replace(), or other string methods.
- Don't hardcode "IN" in your print() statement. Extract it from product_code.
'''


product_code = "AMZ-84729-IN"

print(product_code[-2:])