x = 10
y = 20

x, y = y, x

print(x)
print(y)

'''
Step 1
x = 10
y = 20

Memory:

x → 10
y → 20
Step 2

Python sees:

x, y = y, x

It does NOT immediately assign values.

Instead, it first evaluates the right-hand side.

y, x

Current values are:

y = 20
x = 10

So Python temporarily creates:

Temporary Values

(20, 10)

Memory is still:

x → 10
y → 20
Step 3

Now Python assigns the first temporary value.

x = 20

Memory:

x → 20
y → 20

(For a tiny moment, both are 20.)

Step 4

Now Python assigns the second temporary value.

y = 10


Memory:

x → 20
y → 10
Step 5
print(x)
print(y)

Output:

20
10
Visual Timeline
Initially

x → 10
y → 20

Python remembers

(20, 10)

↓

Assign x

x → 20
y → 20

↓

Assign y

x → 20
y → 10

↓

Final Output

20
10

🧠 Golden Rule

Whenever you see:

a, b = b, a

Always think:

Step 1:
Python remembers the right side.

↓

Step 2:
Python updates the left side.

Never think:

a = b
b = a

because if Python worked like that, the swap would fail.

This Step-by-Step Memory Trace is the exact technique we'll use throughout revision. Once you master this way of tracing variables, even tricky interview questions become much easier to solve. 💪
'''