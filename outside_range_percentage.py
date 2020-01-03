
temp_list = [5,4,3,6,7]
outside_range = []
value_out = 0
value_in = 0
percentage = 0
for item in temp_list:
    if item <0 or item >5:
        outside_range = outside_range + [item]

value_out = len(outside_range)
value_in = len(temp_list)
percentage = (value_out / value_in * 100)
percentage = round(percentage//1)
print(percentage, "% of values are outside the range")



