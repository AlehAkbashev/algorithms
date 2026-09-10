"""https://contest.yandex.ru/contest/27393/problems/H/"""


def main():
    """
    a - интервал на первом пути
    b - интервал на втором пути
    n - количество увиденных поездов на первом пути
    m - количество увиденных поездов на втором пути
    """

    a = int(input())
    b = int(input())
    n = int(input())
    m = int(input())

    t1_min = (1 + a) * n - a    # n + a * (n - 1) (n поездов по одной минут и n-1 перерывов между ними)
    t1_max = a + (1 + a) * n    # n + a * (n + 1) (n поездов по одной минут и n + 1 перерывов, включая до и после)

    t2_min = (1 + b) * m - b
    t2_max = b + (1 + b) * m

    left_boundary = max(t1_min, t2_min)
    right_boundary = min(t1_max, t2_max)

    if left_boundary <= right_boundary:
        print(left_boundary, right_boundary)
        return
    else:
        print(-1)
        return


if __name__ == "__main__":
    main()