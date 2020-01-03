for row in range(9):
    for col in range(5):
        if ((row ==0 or row==4 or row==8) and col not in(0,4)) or (col ==0 and row not in(0,4,5,6,8)) or (col==4 and row not in(0,2,3,4,8)):
            print("*", end="")
        else:
            print(" ", end="")
    print()
