response_times = [120, 450, 80, 600, 200]

for time in response_times:
    if time > 300:
        response_times.remove(time)

print(response_times)