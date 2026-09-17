"""https://contest.yandex.ru/contest/27472/problems/A/"""


def main():

    sequence = list(map(int, input().split()))

    for i in range(1, len(sequence)):
        if sequence[i] > sequence[i-1]:
            continue
        else:
            print("NO")
            return

    print("YES")


if __name__ == "__main__":
    main()