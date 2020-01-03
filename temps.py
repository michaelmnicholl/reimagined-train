daily_temps = [28, 33, 29, 32, 27]
hot_days = []

for temp in daily_temps:
    if temp >20:
        hot_days = hot_days + [temp]
print(len(hot_days))
