text = "Automation"

print(text[:4])
print(text[4:])

'''
A   U   T   O   M   A   T   I   O   N
0   1   2   3   4   5   6   7   8   9
-10 -9 -8  -7  -6  -5  -4  -3  -2  -1 

First Statement
print(text[:4])

When Python sees:

text[:4]

it means:

text[0:4]

Start = 0 (default)

End = 4 (NOT INCLUDED)

So Python takes:

0  1  2  3
A  u  t  o

Stops before index 4.

Output:

Auto
Second Statement
print(text[4:])

This means:

text[4:10]

(Start at index 4 and go till the end.)

Characters are:

4  5  6  7  8  9
m  a  t  i  o  n

Output:

mation
Final Output
Auto
mation

✅ Correct Answer: A

⭐ The Golden Rule of Slicing

Whenever you see:

text[start:end]

Always remember:

✅ Start Index → INCLUDED
❌ End Index   → EXCLUDED
'''