temp_list = [4.7,3,4.8,5,8.5]
best_pos = 0

for item in range(1, len(temp_list)):
    if item > best_pos:
        best_pos = item
print(best_pos, ":00")
