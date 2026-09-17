a = int(input())
b = int(input())
c = int(input())


def triIsExist(A, B, C):
    if A + B > C and B + C > A and A + C > B:
        return 'YES'
    else:
        return 'NO'


print(triIsExist(a, b, c))
