"""https://contest.yandex.ru/contest/27472/problems/B/"""


def main():
    is_ascending = False
    is_descending = False
    is_equal = False

    first_input = int(input())
    if first_input == - 2 * 10 ** 9:
        print("CONSTANT")
        return

    n_previous = first_input

    while (n := int(input())) != -2 * 10 ** 9:
        if n > n_previous:
            is_ascending = True
        elif n == n_previous:
            is_equal = True
        else:
            is_descending = True
        n_previous = n


    if is_descending and is_ascending:
        print("RANDOM")
    elif is_ascending and is_equal:
        print("WEAKLY ASCENDING")
    elif list([is_ascending, is_descending, is_equal]).count(False) == 3:
        print("CONSTANT")
    elif is_ascending:
        print("ASCENDING")
    elif is_descending and is_equal:
        print("WEAKLY DESCENDING")
    elif is_descending:
        print("DESCENDING")
    else:
        print("CONSTANT")





if __name__ == "__main__":
    main()