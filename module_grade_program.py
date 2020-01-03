marks = [0,55,47,67]
lowest = marks[0]
mean = 0

if len(marks) < 3:
    print("Fail")
    print("Your score is below the threshold and you have failed the course")
    exit()
for item in marks:
    if item < lowest:
        lowest = item
for item in marks:
    mean = mean + item
mean = mean - lowest
mean = mean / 3
print(mean)
if mean >=40:
    print("You have passed the course")
elif mean >=30 and mean <=39:
    print("Resit required")
else:
    print("Your score is below the threshold and you have failed the course")
    

