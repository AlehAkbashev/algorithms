"""https://contest.yandex.ru/contest/27393/problems/G/"""



def main():

    """
    N - масса сплава
    K - масса заготовки
    M - масса детали
    """

    N, K, M = map(int, input().split())


    number_of_detail = 0

    while N >= K and K >= M:

        number_of_sample = N // K
        alloy_after_detail = (K % M) * number_of_sample

        N = N - number_of_sample * K + alloy_after_detail
        number_of_detail += number_of_sample * (K // M)

    print(number_of_detail)

if __name__ == "__main__":
    main()