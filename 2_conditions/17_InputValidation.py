'''
Challenge 8 — Input Validation
A registration system accepts usernames only when they contain at least 5 characters and are not empty.

username = "Uday"


Your task:
- If the username is empty, print "Username Required".
- If it contains fewer than 5 characters, print "Username Too Short".
- Otherwise, print "Username Accepted".
Use if-elif-else and a string condition. Write the code yourself, buddy! 😎

'''

username = "udayk"

if len(username) == 0:
    print("Username Required")
elif len(username) < 5:
    print("Username Too Short")
else:
    print("Username Accepted")