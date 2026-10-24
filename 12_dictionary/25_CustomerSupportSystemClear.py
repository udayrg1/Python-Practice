'''
🐍 Day 8 — Challenge: clear()
Scenario: Customer Support System

A support team maintains a dictionary of currently assigned tickets.

support_tickets = {
    "TKT101": "Login Issue",
    "TKT102": "Payment Failure",
    "TKT103": "Page Not Loading",
    "TKT104": "Account Locked"
}

Your requirements
1. Print the original support tickets.
2. Use clear() to remove all tickets from the dictionary.
3. Print the dictionary after clearing it.
4. Print how many tickets remain using len().

Expected output:
{'TKT101': 'Login Issue', 'TKT102': 'Payment Failure', 'TKT103': 'Page Not Loading', 'TKT104': 'Account Locked'}
{}
0
'''

support_tickets = {
    "TKT101": "Login Issue",
    "TKT102": "Payment Failure",
    "TKT103": "Page Not Loading",
    "TKT104": "Account Locked"
}

print(support_tickets)

support_tickets.clear()

print(support_tickets)

print(len(support_tickets))