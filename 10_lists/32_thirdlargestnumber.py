#Give an array of integers, find the 3rd largest element in the array

arr = [7, 10, 4, 3, 20, 15]

largest_num = None
second_largest = None
third_largest = None

arr = [7, 10, 4, 3, 20, 15]

largest_num = None
second_largest = None
third_largest = None

for num in arr:

    if num == largest_num or num == second_largest or num == third_largest:
        continue

    if largest_num is None or num > largest_num:
        third_largest = second_largest
        second_largest = largest_num
        largest_num = num

    elif second_largest is None or num > second_largest:
        third_largest = second_largest
        second_largest = num

    elif third_largest is None or num > third_largest:
        third_largest = num

if third_largest is not None:
    print(third_largest)
else:
    print("There are fewer than three distinct numbers.")