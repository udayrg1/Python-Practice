'''
Challenge 6 — Multiple Conditions with or
A login system allows a user to log in if they authenticate using either a password or an OTP.

password_valid = False
otp_valid = True

Your task: Write an if-else statement:
- If either password_valid or otp_valid is True, print "Login Successful".
- If both are False, print "Login Failed".
Use the logical operator or

'''

password_valid = False
otp_valid = True

if password_valid or otp_valid:
    print("Login Successful")
else:
    print("Login Failed")