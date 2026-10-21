'''
Next is String Challenge 16 — .startswith()
url = "https://www.amazon.in/product/12345"



Write a program to check whether the URL starts with "https://" and print:
Secure URL


If it doesn't, print:
Not a secure URL


Rule: Use .startswith() with if/else. No shortcuts, da! 💪
'''

url = "https://www.amazon.in/product/12345"

if url.startswith("https://"):
    print("Secure URL")
else:
    print("Not a secure URL")