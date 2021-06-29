''' '''

from gf256 import mul


class AEStables:

    def __init__(self):
        #
        self._E = bytearray(256)
        self._L = bytearray(256)
        self._S = bytearray(256)
        self._invS = bytearray(256)
        self._inv = bytearray(256)
        self._powX = bytearray(256)

        self.load_e()
        self.load_l()
        self.load_inv()
        self.load_s()
        self.load_inv_s()
        self.load_pow_x()

    def s_box(self, b):
        #
        assert 0 <= b <= 255

        return self._S[b & 0xFF]

    def inv_s_box(self, b):
        #
        assert 0 <= b <= 255

        return self._invS[b & 0xFF]

    def r_con(self, i: int):
        #
        return self._powX[i - 1]

    def load_e(self):
        #
        x = 0x01
        index = 0
        self._E[index] = 0x01
        index += 1
        # or 256 ?
        for _ in range(255):
            y = mul(x, 0x03)
            self._E[index] = y
            index += 1
            x = y

    def load_l(self):
        #
        for i in range(256):
            self._L[self._E[i] & 0xFF] = i

    def load_s(self):
        #
        for i in range(256):
            self._S[i] = self.sub_bytes(i & 0xFF)

    def load_inv(self):
        #
        for i in range(256):
            self._inv[i] = self.ff_inv(i & 0xFF)

    def load_inv_s(self):
        #
        for i in range(256):
            self._invS[self._S[i] & 0xFF] = i

    def load_pow_x(self):
        #
        x = 0x02
        xp = x
        self._powX[0] = 1
        self._powX[1] = x
        for i in range(2, 15):
            xp = mul(xp, x)
            self._powX[i] = xp

    def ff_inv(self, b):
        #
        assert 0 <= b <= 255
        e = self._L[b & 0xFF]

        return self._E[0xFF - (e & 0xFF)]

    def ith_bit(self, b, i):
        #
        assert 0 <= b <= 255
        m = [0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80]
        return (b & m[i]) >> i

    def sub_bytes(self, b):
        #
        assert 0 <= b <= 255

        if b != 0:
            b = self.ff_inv(b) & 0xFF

        c = 0x63
        res = 0
        for i in range(8):
            t = self.ith_bit(b, i) ^ self.ith_bit(b, (i + 4) % 8)
            t ^= self.ith_bit(b, (i + 5) % 8)
            t ^= self.ith_bit(b, (i + 6) % 8)
            t ^= self.ith_bit(b, (i + 7) % 8)
            t ^= self.ith_bit(c, i)
            res |= (t << i)

        return res
