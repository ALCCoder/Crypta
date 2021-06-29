import math


def find_all_simple_divider(m: int):
    #
    if m < 2:
        return []

    result = [2]
    for i in range(3, m, 2):

        if i > 10 and i % 10 == 5:
            continue

        f = False
        for j in range(len(result)):

            if result[j] ** 2 - 1 > i:
                f = True
                result.append(i)
                break

            if i % result[j] == 0:
                f = True
                break

        if not f:
            result.append(i)

    return result


def euclid_ex_bin(a, b):
    #
    g = 1

    while (a & 1) == 0 and (b & 1) == 0:
        a >>= 1
        b >>= 1
        g <<= 1

    u, v = a, b
    A, B, C, D = 1, 0, 0, 1

    while u != 0:
        while (u & 1) == 0:
            u >>= 1

            if (A & 1) == 0 and (B & 1) == 0:
                A >>= 1
                B >>= 1
            else:
                A = (A + b) >> 1
                B = (B - a) >> 1

        while (v & 1) == 0:
            v >>= 1

            if (C & 1) == 0 and (D & 1) == 0:
                C >>= 1
                D >>= 1
            else:
                C = (C + b) >> 1
                D = (D - a) >> 1

        if u >= v:
            u -= v
            A -= C
            B -= D
        else:
            v -= u
            C -= A
            D -= B

    x = C
    y = D

    return g * v, x, y


def euclid(a, b):
    #
    while b > 0:
        a %= b
        a, b = b, a

    return a


def gcd(a, b):
    x, y, x1, y1 = 1, 0, 0, 1
    while b:
        q = a // b
        a, b = b, a % b
        x, x1 = x1, x - x1 * q
        y, y1 = y1, y - y1 * q
    return (a, x, y)


def euler(n: int):
    #
    res = n
    for i in range(1, n):
        if euclid(i, n) != 1:
            res -= 1

    return res - 1


def red_deduction_system(n: int):
    #
    res = []
    for i in range(1, n):
        if euclid(i, n) == 1:
            res.append(i)

    return res


def fast_pow_mod(a, b, n):
    #
    res = 1
    while b > 0:
        if b & 1:
            res = (res * a) % n
        a = (a ** 2) % n
        b >>= 1

    return res


def factorization(n: int):
    #
    res = []
    i = 2
    while i < math.sqrt(n):
        if n % i == 0:
            while n % i == 0:
                n //= i
                res.append(i)
        i += 1

    if n != 1:
        res.append(n)

    return res


def mult_inverse(a, m):
    g, x, _ = euclid_ex_bin(a, m)

    if g != 1:
        raise AttributeError('Not exist')

    x %= m

    return x


if __name__ == "__main__":
    print(factorization(144))
