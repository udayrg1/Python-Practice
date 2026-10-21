daily_readings = [12, 18, 25, 9, 30]

for index, value in enumerate(daily_readings):
    if value < 15:
        daily_readings[index] = 15

print(daily_readings)
