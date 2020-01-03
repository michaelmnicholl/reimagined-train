temp_cel = [-10, -20, -30]
temp_far = []

for each_position in temp_cel:
    faren = (each_position * 9/5) + 32
    temp_far = temp_far + [faren]
print(temp_far)


