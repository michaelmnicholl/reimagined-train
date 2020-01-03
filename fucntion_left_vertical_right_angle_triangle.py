x = int(input("Enter your triangle size as a number: "))

def tri_ast(x):

    """print left vertical right angled triangle like this
    *
    **
    * *
    *  *
    *****
    """

    for row in range(x):
        for col in range(x):
            if row == 4 or col == 0 or row == col:
                print("*", end="")
            else:
                print(" ", end="")
        print()

