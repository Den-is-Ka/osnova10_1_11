
def add_numbers(a, b):
    return a+b


def is_even(a):
    return a % 2 == 0


def find_max(my_list):
    return max(my_list)


if __name__ == '__main__':
    assert add_numbers(2, 2) == 4

    assert is_even(2) == True

    assert find_max([1, 2, 3, 4, 5]) == 5

    # from src.utils import reverse_text
    #
    # if __name__ == '__main__':
    #     reverse_text('кораблик')
