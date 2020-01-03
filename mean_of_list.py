list = [2, 4, 6, 8, 10]
mean = 0


for item in list:
    mean = mean + item
mean = mean / len(list)
print(int(mean))
