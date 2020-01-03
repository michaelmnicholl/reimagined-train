def integer_0_or_1(x):
    """convert false to 0 and true to 1"""
    if x == True:
        integer_0_or_1 = 1
    else:
        integer_0_or_1 = 0
    return integer_0_or_1

    

def and_binary(A, B):
    if A == True and B == True:
        output = 1
    else:
        output = 0
    return output
