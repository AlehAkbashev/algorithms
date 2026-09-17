"""https://contest.yandex.ru/contest/27472/problems/D/"""


def main():

    numbers = list(map(int, input().split()))
    counter = 0

    if len(numbers) < 3:
        print(counter)
        return

    for i in range(1, len(numbers) - 1):
        if numbers[i - 1] < numbers[i] > numbers[i + 1]:
            counter += 1

    print(counter)
    return

if __name__ == "__main__":
    main()