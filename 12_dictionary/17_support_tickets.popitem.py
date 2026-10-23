'''
Day 8 — popitem() Unique Challenge
Now let's apply this method to a different problem: processing the latest support tickets first.

A support team stores incoming tickets in a dictionary:
support_tickets = {    "TKT501": "Password reset",    "TKT502": "Payment failure",    "TKT503": "Login issue",    "TKT504": "Order cancellation",    "TKT505": "Delivery delay"}


Your requirements
1. Process and remove the latest three tickets using popitem().
2. Store each removed ticket in a separate variable.
3. Print the three removed tickets in the order they were processed.
4. Print the remaining support tickets.
5. Print how many tickets remain.
Rules
- Use popitem() to remove each ticket.
- Do not use pop(), del, or loops.
- Do not modify the original dictionary manually.
- Write the complete program yourself.

'''

support_tickets = {
    "TKT501": "Password reset",
    "TKT502": "Payment failure",
    "TKT503": "Login issue",
    "TKT504": "Order cancellation",
    "TKT505": "Delivery delay"
}

first_ticket = support_tickets.popitem()
second_ticket = support_tickets.popitem()
third_ticket = support_tickets.popitem()

print(first_ticket)
print(second_ticket)
print(third_ticket)

print(support_tickets)

print(len(support_tickets))