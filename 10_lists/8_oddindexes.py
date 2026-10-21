'''
Day 5 — Next problem
Given this list, print all values at odd indexes without using default methods.

numbers = [12, 25, 34, 47, 56, 69, 78, 81]

Expected output:

[25, 47, 69, 81]
'''

#ODD INDEX

numbers = [12, 25, 34, 47, 56, 69, 78, 81]
#           0   1   2   3   4   5   6   7

odd_index_num = []

for i in range(1, len(numbers), 2):
    odd_index_num.append(numbers[i])

print("Odd Index Num: ", odd_index_num)


#EVEN INDEX

numbers = [12, 25, 34, 47, 56, 69, 78, 81]
#           0   1   2   3   4   5   6   7

even_index_num = []

for i in range(0, len(numbers), 2):
    even_index_num.append(numbers[i])

print("Even Index Num: ", even_index_num)



#ODD INDEX

numbers = [12, 25, 34, 47, 56, 69, 78, 81]
#           0   1   2   3   4   5   6   7

odd_index_numbers = [0] * len(numbers)
index = 0

for i in range(1, len(numbers), 2):
    odd_index_numbers[index] = numbers[i]
    index += 1

print("Odd Index Values:", odd_index_numbers[:index])

#EVEN INDEX

numbers = [12, 25, 34, 47, 56, 69, 78, 81]
#           0   1   2   3   4   5   6   7

even_index_numbers = [0] * len(numbers)
index = 0

for i in range(0, len(numbers), 2):
    even_index_numbers[index] = numbers[i]
    index += 1

print("Even Index Values:", even_index_numbers[:index])