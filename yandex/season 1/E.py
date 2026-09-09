"""https://contest.yandex.ru/contest/27393/problems/E/"""


def main():
    """
    K1 - номер квартиры
    M - количество этажей
    К2 - номер квартиры 
    Р2 - номер подъезда квартиры К2
    N2 - номер этажа квартиры К2

    Найти Р1, N1
    """
    K1, M, K2, P2, N2 = map(int, input().split())

    if N2 > M:
        print(-1, -1)
        return

    floors_before_K2 = (P2 - 1) * M + N2 - 1
    floors_inlcuding_K2 = (P2 - 1) * M + N2

    max_rooms = max(K1, K2) + 1

    set_N = set()
    set_P = set()

    for X in range(1, max_rooms + 1):

        cond_1 = K2 > floors_before_K2 * X
        cond_2 = K2 <= floors_inlcuding_K2 * X

        if cond_1 and cond_2:

            floor_before_K1 = (K1 - 1) // X

            P1 = floor_before_K1 // M + 1
            N1 = floor_before_K1 % M + 1

            set_N.add(N1)
            set_P.add(P1)

    if len(set_N) == 0:
        print(-1, -1)
        return

    ans_N1 = list(set_N)[0] if len(set_N) == 1 else 0
    ans_P1 = list(set_P)[0] if len(set_P) == 1 else 0

    print(ans_P1, ans_N1)
    return



if __name__ == "__main__":
    main()