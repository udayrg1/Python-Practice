"""
Question 2: Username Cleanup

Problem

The username contains unnecessary spaces.

"    Uday Kumar    "

Remove the spaces and print:

Welcome Uday Kumar

"""
#main program
username = "   Uday Kumar   "

clean_name = username.strip()

print(f"Welcome {clean_name}")

"""
strip() - method

removes spaces from

left
right

It does NOT remove spaces between words.

"""