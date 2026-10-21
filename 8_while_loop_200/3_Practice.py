'''
🐍⚔️ Q3/200 — Consecutive Failure Limit

Write a Python program that:

Uses a while loop
Keeps asking the user to enter a password
The correct password is "python123"
The user gets a maximum of 3 attempts
If the password is correct → print "Access Granted" and stop
If all 3 attempts are wrong → print "Access Denied"
Must use break
Don't use a list

💡 New concept: limited-attempt loop + success/failure state.
'''
correct_password = "python123"

found = False
retry = 1

while retry <= 3:
    password_input = input("Enter a password: ")

    if password_input == correct_password:
        print("Access Granted")
        found = True
        break
    else:
        retry += 1

if not found:
    print("Access Denied")

