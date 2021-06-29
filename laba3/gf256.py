def get_bit(a, k):
    return (a >> k) & 1


def to_polynom_form(item):
    #
    assert 0 <= item <= 255
    res = ''
    for i in range(7, -1, -1):
        if get_bit(item, i):
            res += f'x^{i}+'

    res = res.replace('x^0', '1')
    res = res.replace('x^1', 'x')
    res = res[:-1]

    return res


def mul(a, b):
    #
    assert 0 <= a <= 255
    assert 0 <= b <= 255

    aa, bb, r, t = a, b, 0, 0
    while aa != 0:
        if (aa & 1) != 0:
            r ^= bb

        t = bb & 0x80
        bb <<= 1

        if t != 0:
            bb ^= 0x1b
        aa >>= 1

    return r & 0xFF


def inv(a):
    return _pow(a, 254)


def _pow(a, n):
    assert 0 <= a <= 255

    res = a

    while n > 1:
        n -= 1
        res = mul(res, a)

    return res


if __name__ == "__main__":
    # print(to_polynom_form(1))
    print(mul(inv(12), 12))
