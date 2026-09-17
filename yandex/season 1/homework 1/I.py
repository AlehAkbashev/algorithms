"""https://contest.yandex.ru/contest/27393/problems/I/"""


def main():

    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    E = int(input())


    hole = sorted((D, E))
    brick = sorted((A, B, C))

    if brick[0] <= hole[0] and brick[1] <= hole[1]:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    main()