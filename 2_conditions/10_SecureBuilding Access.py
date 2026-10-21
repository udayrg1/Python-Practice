'''
A company building has an electronic access system. A person can enter only if both conditions are satisfied:
- They have a valid access card.
- Their security training is completed.
Given:
valid_card = Truetraining_completed = False



Your task: Write a Python program that prints:
- "Access Granted" if both conditions are satisfied.
- "Access Denied" otherwise.
Rules: Use conditional logic with a logical operator. No loops, no functions, and no hints unless you ask!
'''

valid_card = True
training_completed = False

if (valid_card and training_completed == True):
    print("Access Granted")
else:
    print("Access Denied")