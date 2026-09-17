"""https://contest.yandex.ru/contest/27393/problems/J/"""


def main():
    a1 = float(input())
    b1 = float(input())
    a2 = float(input())
    b2 = float(input())
    c1 = float(input())
    c2 = float(input())

    D = a1 * b2 - b1 * a2
    Dx = c1 * b2 - b1 * c2
    Dy = a1 * c2 - c1 * a2

    if D == 0:
        if Dx != 0 or Dy != 0:
            print(f"0")
            return
        else:
            if a1 == 0 and b1 == 0 and c1 == 0:
                a1, b1, c1 = a2, b2, c2

            if a1 == 0 and b1 == 0:
                if c1 == 0:
                    print(5)
                    return
                else:
                    print(0)
                    return
            elif a1 == 0 and b1 != 0:
                y = c1 / b1
                print(f"4 {y:.5f}")
                return
            elif a1 != 0 and b1 == 0:
                x = c1 / a1
                print(f"3 {x:.5f}")
                return
            else:
                k = -a1/b1
                n = c1/b1
                print(f"1 {k:.5f} {n:.5f}")
                return
    else:
        x = Dx / D
        y = Dy / D
        print(f"2 {x:.5f} {y:.5f}")
        return

if __name__ == "__main__":
    main()