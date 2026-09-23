"""https://contest.yandex.ru/contest/27472/problems/E/"""


def main():
    n = int(input())

    scoreboard = list(map(int, input().split()))

    max_vasya_result = -1
    winner_score = max(scoreboard)
    was_winner_before = False


    for i in range(n - 1):
        if scoreboard[i] == winner_score and was_winner_before == False:
            was_winner_before = True
            continue

        if scoreboard[i] % 10 == 5 and scoreboard[i+1] < scoreboard[i] and was_winner_before:
            if scoreboard[i] > max_vasya_result:
                max_vasya_result = scoreboard[i]


    if max_vasya_result == -1:
        print(0)
        return

    higher_than_vasya = 0

    for i in range(n):
        if max_vasya_result < scoreboard[i]:
            higher_than_vasya += 1

    print(higher_than_vasya + 1)
    return
        


if __name__ == "__main__":
    main()