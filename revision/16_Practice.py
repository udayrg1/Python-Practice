text = "Automation"

print(text[::2])

'''
Indexing Table
Character :  A   u   t   o   m   a   t   i   o   n
Positive  :  0   1   2   3   4   5   6   7   8   9
Options

A)

Atoain

B)

Atmto

C)

Atoatn

D)

Automation

Slice
text[::2]

Python interprets it as:

text[0:10:2]

Meaning:

✅ Start = Beginning
✅ End = End of string
✅ Step = 2

So Python picks every 2nd character.

Let's mark them.

Character :  A   u   t   o   m   a   t   i   o   n
Index     :  0   1   2   3   4   5   6   7   8   9
             ✔       ✔       ✔       ✔       ✔

Selected characters:

A   t   m   t   o

Output:

Atmto
🧠 Slicing Formula
text[start:end:step]
'''

