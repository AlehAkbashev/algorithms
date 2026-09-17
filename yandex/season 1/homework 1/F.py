"""https://contest.yandex.ru/contest/27393/problems/F/"""


def main():

    A, B, C, D = map(int, input().split())

    variations = [
        (A + C, max(B, D)),
        (B + D, max(A, C)),
        (B + C, max(A, D)),
        (A + D, max(B, C))
    ]

    best_table = variations[0]
    min_square = best_table[0] * best_table[1]

    for item in variations:
        current_square = item[0] * item[1]
        if current_square < min_square:
            best_table = item
            min_square = current_square

    print(best_table[0], best_table[1])
    return


    

if __name__ == "__main__":
    main()