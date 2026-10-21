'''
🎯 Function Practice #7 — Password Validator

This one is intentionally different from the previous programs.

Create:
validate_password(password)
Requirements

The function should return:

"Valid Password" if:
password has at least 8 characters
AND contains at least one digit
"Invalid Password" otherwise.

Test with:
python123
python
hello123

Expected output
Valid Password
Invalid Password
Valid Password
'''

def validate_password(password):

    if len(password) >= 8:
        for character in password:
            if character.isdigit():
                return "Valid Password"

    return "Invalid Password"


print(validate_password("python123"))
print(validate_password("python"))
print(validate_password("hello123"))