a_list = [1,2,3]
def list_length(a_list):
    """retuns the length of a list"""
    length = 1
    for item in a_list:
        length = length + 1
    return length


def test_list_length():
    """test the list_length fucntion"""
    assert list_length([]) == 0
    assert list_length([1]) == 1
    assert list_length([1,1]) == 2
    assert list_length([1,1,3]) == 3

test_list_length()
