from aes_tables import AESTables
import numpy as np
from gf256 import mul


class AES:

    def __init__(self, key: bytearray, nk_in: int):
        #
        self._Nb = 4
        self._Nk = nk_in
        self._Nr = nk_in + 6
        self._w_count = 0
        self._tab = AESTables()
        self._w = bytearray(4 * self._Nb * (self._Nr + 1))
        self.key_expansion(key, self._w)

    def encode_block(self, input: bytearray):
        #
        self._w_count = 0
        state = self.copy_to_arr(input)
        self.add_round_key(state)

        for _ in range(1, self._Nr):
            self.sub_bytes(state)
            self.shift_rows(state)
            self.mix_columns(state)
            self.add_round_key(state)

        self.sub_bytes(state)
        self.shift_rows(state)
        self.add_round_key(state)
        output = self.copy_to_list(state)

        return output

    def decode_block(self, input):
        self._w_count = 4 * self._Nb * (self._Nr + 1)
        state = self.copy_to_arr(input)
        self.inv_add_round_key(state)

        for _ in range(self._Nr - 1, 0, -1):
            self.inv_shift_rows(state)
            self.inv_sub_bytes(state)
            self.inv_add_round_key(state)
            self.inv_mix_columns(state)

        self.inv_shift_rows(state)
        self.inv_sub_bytes(state)
        self.inv_add_round_key(state)
        out = self.copy_to_list(state)

        return out

    def key_expansion(self, key, w):
        tmp = bytearray([0 for i in range(4 * self._Nb * (self._Nr + 1))])
        j = 0

        while j < self._Nk * 4:
            w[j] = key[j]
            j += 1

        while j < 4 * self._Nb * (self._Nr + 1):
            i = j // 4

            for i_tmp in range(4):
                tmp[i_tmp] = w[j - 4 + i_tmp]

            if i % self._Nk == 0:
                old_temp_0 = tmp[0]

                for i_tmp in range(4):
                    ttmp, trcon = 0, 0

                    if i_tmp == 3:
                        ttmp = old_temp_0
                    else:
                        ttmp = tmp[i_tmp + 1]
                    if i_tmp == 0:
                        trcon = self._tab.r_con(i // self._Nk)
                    else:
                        trcon = 0
                    tmp[i_tmp] = self._tab.s_box(ttmp) ^ trcon

            elif self._Nk > 6 and (i % self._Nk) == 4:
                for i_tmp in range(4):
                    tmp[i_tmp] = self._tab.s_box(tmp[i_tmp])

            for i_tmp in range(4):
                w[j + i_tmp] = w[j - 4 * self._Nk + i_tmp] ^ tmp[i_tmp]

            j += 4

    def sub_bytes(self, state):
        #
        for i in range(4):
            for j in range(self._Nb):
                state[i][j] = self._tab.s_box(state[i][j])

    def shift_rows(self, state):
        #
        t = bytearray(4)
        for i in range(1, 4):
            for c in range(self._Nb):
                t[c] = state[i][(c + i) % self._Nb]
            for c in range(self._Nb):
                state[i][c] = t[c]

    def mix_columns(self, s):
        #
        sp = bytearray(4)
        b02 = 0x02
        b03 = 0x03
        for c in range(4):
            sp[0] = (mul(b02, s[0][c]) ^ mul(b03, s[1][c]) ^
                     s[2][c] ^ s[3][c])
            sp[1] = (s[0][c] ^ mul(b02, s[1][c]) ^
                     mul(b03, s[2][c]) ^ s[3][c])
            sp[2] = (s[0][c] ^ s[1][c] ^
                     mul(b02, s[0][c]) ^ mul(b03, s[3][c]))
            sp[3] = (mul(b03, s[0][c]) ^ s[1][c] ^
                     s[2][c] ^ mul(b02, s[3][c]))

            for i in range(4):
                s[i][c] = sp[i]

    def add_round_key(self, state):
        #
        for c in range(self._Nb):
            for i in range(4):
                state[i][c] = state[i][c] ^ self._w[self._w_count]
                self._w_count += 1

    def inv_sub_bytes(self, state):
        #
        for i in range(4):
            for j in range(self._Nb):
                state[i][j] = self._tab.inv_s_box(state[i][j])

    def inv_shift_rows(self, state):
        #
        t = bytearray(4)
        for i in range(1, 4):
            for c in range(self._Nb):
                t[(c + i) % self._Nb] = state[i][c]
            for c in range(self._Nb):
                state[i][c] = t[c]

    def inv_mix_columns(self, s):
        #
        sp = bytearray(4)
        b0b = 0x0b
        b0d = 0x0d
        b09 = 0x09
        b0e = 0x0e
        for c in range(4):
            sp[0] = (mul(b0e, s[0][c]) ^ mul(b0b, s[1][c]) ^
                     mul(b0d, s[2][c]) ^ mul(b09, s[3][c]))
            sp[1] = (mul(b09, s[0][c]) ^ mul(b0e, s[1][c]) ^
                     mul(b0b, s[2][c]) ^ mul(b0d, s[3][c]))
            sp[2] = (mul(b0d, s[0][c]) ^ mul(b09, s[1][c]) ^
                     mul(b0e, s[2][c]) ^ mul(b0b, s[3][c]))
            sp[3] = (mul(b0b, s[0][c]) ^ mul(b0d, s[1][c]) ^
                     mul(b09, s[2][c]) ^ mul(b0e, s[3][c]))

            for i in range(4):
                s[i][c] = sp[i]

    def inv_add_round_key(self, state):
        #
        for c in range(self._Nb-1, -1, -1):
            for i in range(3, -1, -1):
                self._w_count -= 1
                state[i][c] = state[i][c] ^ self._w[self._w_count]

    def copy_to_list(self, state):
        out = bytearray()

        for line in state:
            for b in line:
                out.append(b)

        return out

    def copy_to_arr(self, b_arr):
        # state = np.resize(np.array(b_arr), (4, self._nb))

        # return state
        state = []
        k = 0
        for _ in range(self._Nb):
            line = []
            for _ in range(4):
                line.append(b_arr[k])
                k += 1
            state.append(line)

        return state


if __name__ == "__main__":
    aes = AES([x for x in range(16)], 4)
    message = 'ABCDEFGHKLDSIKLP'
    enc_message = message.encode('utf-8')
    enc = aes.encode_block(enc_message)
    res = aes.decode_block(enc)
    print(res.decode('utf-8'))
