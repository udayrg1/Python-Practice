text = "Automation"

print(text[:-4])

'''
Character :  A   u   t   o   m   a   t   i   o   n
Positive  :  0   1   2   3   4   5   6   7   8   9
Negative  : -10 -9  -8  -7  -6  -5  -4  -3  -2  -1

Options

A)

Automa

B)

Auto

C)

Automation

D)

mation

Slice
text[:-4]

Python converts this to:

text[0:-4]

This means:

✅ Start = 0 (included)
❌ End = -4 (excluded)

Let's mark it:

Character :  A   u   t   o   m   a   t   i   o   n
Positive  :  0   1   2   3   4   5   6   7   8   9
Negative  : -10 -9  -8  -7  -6  -5  -4  -3  -2  -1
            ✔   ✔   ✔   ✔   ✔   ✔ ✘

Selected characters:

A  u  t  o  m  a

Output:

Automa
'''