sensor_readings = [14, 0, 22, -1, 31, 0, 18]

'''
Create a new list containing only valid readings, preserving their original order.
Calculate the average of those valid readings.
Print both the valid readings and their average.
'''

valid_readings = []

for digit in sensor_readings:
    if digit > 0:
        valid_readings.append(digit)

average = (sum(valid_readings)/len(valid_readings))


print("Valid Readings: ", valid_readings)
print("Average: ", average)