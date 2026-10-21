'''
Challenge 2 — Unique concept: Independent decisions 🚦
A delivery monitoring system tracks two separate events:

package_delayed = True
payment_received = True



Your task:
- If the package is delayed, print "Notify Customer About Delay".
- If payment has been received, print "Generate Payment Receipt".
- Both messages should appear when both conditions are True.
Requirement: Use two independent if statements, not an if-else chain.
'''


package_delayed = True
payment_received = True

if package_delayed == False:
    print("Notify Customer About Delay")
    
if payment_received == True:
    print("Generate Payment Receipt")