"""https://contest.yandex.ru/contest/27472/problems/C/"""


def main():
    N = int(input())

    numbers = map(int, input().split())
    x = int(input())

    min_distance = 1000 * 2 + 2
    for number in numbers:
        distance = abs(number - x)
        if distance == 0:
            answer = number
            break
        elif distance < min_distance:
            min_distance = distance
            answer = number
        

    print(answer)
    return


if __name__ == "__main__":
    main()