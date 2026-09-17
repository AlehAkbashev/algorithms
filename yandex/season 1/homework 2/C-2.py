"""https://contest.yandex.ru/contest/27472/problems/C/"""


def main():
    N = int(input())

    numbers = map(int, input().split())
    x = int(input())

    answer = min(numbers, key=lambda number: abs(x - number))

    print(answer)


if __name__ == "__main__":
    main()