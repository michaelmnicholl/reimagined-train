celsius_values = [-1,0,5,8]
kelvin_values = []

for item in celsius_values:
    kelvin = item + 273.15
    kelvin_values = kelvin_values + [kelvin]
print(kelvin_values)
