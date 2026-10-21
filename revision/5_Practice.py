'''
😈 Question 5 (Interview Favorite)

Predict the output:
'''
a = 5
b = a
c = b

a = 10
b = 20

'''
print(a)
print(b)
print(c)
Options

A)

10
20
5

B)

10
20
20

C)

5
20
5

D)

10
5
5

This one checks whether you understand multiple variable assignments.

Take your time and tell me the output. 😄

'''
'''
Step-by-step Memory Trace

Step 1
a = 5
a → 5

Step 2
b = a
a → 5
b → 5

Step 3
c = b
a → 5
b → 5
c → 5

Step 4
a = 10
a → 10
b → 5
c → 5

Step 5
b = 20
a → 10
b → 20
c → 5

Final Output
print(a)
print(b)
print(c)

10
20
5
'''