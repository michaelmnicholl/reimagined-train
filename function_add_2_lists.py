def list_sum(list_1, list_2):
    x = 0
    y = 0
    for item in list_1:
        x = x + item
    for pos in list_2:
        y = y + pos
    z = x+y
    print("The total sum of both lists is: ", z)

 
