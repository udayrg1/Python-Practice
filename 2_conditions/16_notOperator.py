'''
Challenge 7 — The not Operator 🔄
A deployment system must block deployment when maintenance mode is active.

maintenance_mode = False

Your task:
- If maintenance mode is not active, print "Deployment Allowed".
- Otherwise, print "Deployment Blocked".

Use the not operator explicitly.

'''

maintenance_mode = False

if not maintenance_mode:
    print("Deployment Allowed")
else:
    print("Deployment Blocked")