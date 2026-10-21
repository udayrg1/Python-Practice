"""
Question 9: Full Name Formatter
Problem

Input:

firstname = "uday"

lastname = "ramagiri"

Print

Full Name: Uday Ramagiri
"""


#method_1
firstname = "uday"

lastname = "ramagiri"

updated_firstname = firstname.capitalize()
updated_lastname = lastname.capitalize()

print(f"Full name: {updated_firstname} {updated_lastname}")


#method_2
firstname = "uday"
lastname = "ramagiri"

full_name = firstname.title() + " " + lastname.title()

print(full_name)


#method_3
firstname = "uday"
lastname = "ramagiri"

full_name = f"{firstname.capitalize()} {lastname.capitalize()}"

print(full_name)

#method_4
firstname = "uday"
lastname = "ramagiri"

print(firstname.capitalize(), lastname.capitalize())