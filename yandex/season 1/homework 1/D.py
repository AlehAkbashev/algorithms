"""https://contest.yandex.ru/contest/27393/problems/D/"""


def equal_solution(a,b,c):
    if c < 0:
        return "NO SOLUTION"
    elif a == 0 and (b < 0 or b != c**2):
        return "NO SOLUTION"
    elif a == 0 and b == c**2:
        return "MANY SOLUTIONS"
    else:
        x = (c**2 - b) / a
        if x % 1 == 0:
            return int(x)
        else:
            return "NO SOLUTION"



if __name__ == "__main__":
    a = int(input())
    b = int(input())
    c = int(input())

    print(equal_solution(a,b,c))
